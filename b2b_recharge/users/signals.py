from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CreditRequest


@receiver(post_save, sender=CreditRequest)
def approve_credit_request(sender, instance, **kwargs):
    if instance.approved and not instance._state.adding:
        instance.seller.increase_credit(instance.amount)
