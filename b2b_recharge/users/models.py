from django.db import models, transaction
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)



class Seller(models.Model):
    name = models.CharField(max_length=100)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    @transaction.atomic()
    def increase_credit(self, amount):
        if amount <= 0:
            self.credit += amount
            logger.info(f"Credit decreased by {amount} for seller {self.id}")
            if self.credit < 0:
                self.credit = 0
                logger.info(f"Credit set to 0 for seller {self.id}")
        else:
            self.credit += amount
            logger.info(f"Credit increased by {amount} for seller {self.id}")
        self.save()
        

    def decrease_credit(self, amount):
        if amount > self.credit:
            raise ValueError("Insufficient credit")
        self.credit -= amount
        self.save()
        logger.info(f"Credit decreased by {amount} for seller {self.id}")

    def __str__(self):
        return f"{self.name} - Credit: {self.credit}"


class CreditRequest(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    @transaction.atomic()
    def approve(self):
        if not self.approved:
            self.approved = True
            self.save()

