from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import PurchaseOrder
import logging

signal_logger = logging.getLogger('signal_logger')
file_handler = logging.FileHandler('./signals.log')
signal_logger.addHandler(file_handler)

@receiver(signal=pre_save, sender=PurchaseOrder)
def presave_delivery_date(sender, instance, **kwargs):
    
    #Un-updated object

    purchase_order_obj = PurchaseOrder.objects.get(pk=instance.id)
    old_order_status = purchase_order_obj.status

    #Updated object
    
    new_order_status = instance.status

    
    if not old_order_status == new_order_status:
        signal_logger.debug('works here')