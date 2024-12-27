from django.db import models, transaction
from transactions.models import Transaction
from users.models import Seller

import logging

logger = logging.getLogger(__name__)


class PhoneNumber(models.Model):
    number = models.CharField(max_length=15, unique=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def recharge(self, amount):
        with transaction.atomic():
            seller = Seller.objects.select_for_update().get(pk=self.seller.pk)
            if amount > seller.credit:
                raise ValueError("Insufficient credit")
            seller.decrease_credit(amount)
            transactionـobject = Transaction.objects.create(
                seller=seller,
                transaction_type='DEBIT',
                amount=amount
            )
            logger.info(f"Phone number {self.number} recharged by {amount} for seller {seller.id}")
            return transactionـobject

    def __str__(self):
        return self.number