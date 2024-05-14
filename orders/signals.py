from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import PurchaseOrder

@receiver(signal=pre_save, sender=PurchaseOrder)
def calculate_delivery_rate(sender, instance, **kwargs):
    not_updated_obj = PurchaseOrder.objects.get(pk=instance.id).issue_date

    updated_obj = instance.issue_date

    print("new issue date: ", instance.issue_date)




