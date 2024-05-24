from orders.models import PurchaseOrder
from django.utils import timezone
from datetime import datetime
from .loggers import delivery_date_logger
from vendors.models import VendorPerformance

def calc_ontime_delivery_rate(related_vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=related_vendor.id, status="completed")
    completed_orders_on_time = [ completed_order for completed_order in completed_orders if completed_order.delivery_date>=timezone.now()]

    ontime_delivery_rate = (len(completed_orders_on_time)/len(completed_orders))*100
    related_vendor.on_time_delivery_rate = ontime_delivery_rate

    delivery_date_logger.debug("this is the on time delivery date: ", ontime_delivery_rate)
    return ontime_delivery_rate