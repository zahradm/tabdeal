from django.db import models
from django.utils.timezone import now


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('CREDIT', 'Credit'),
        ('DEBIT', 'Debit'),
    ]
    seller = models.ForeignKey('users.Seller', on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.seller} - {self.transaction_type} - {self.amount}'