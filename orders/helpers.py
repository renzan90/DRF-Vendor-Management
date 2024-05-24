from orders.models import PurchaseOrder
from django.utils import timezone
from datetime import datetime
from .loggers import vms_logger
from vendors.models import VendorPerformance

def calc_ontime_delivery_rate(related_vendor):
    #cache - completed orders and *add current completed order to it
    completed_orders = PurchaseOrder.objects.filter(vendor=related_vendor.id, status="completed")
    
    #cache - completed orders on time value and *add current completed order if completed on time
    completed_orders_on_time = [completed_order for completed_order in completed_orders if completed_order.delivery_date>=timezone.now()]

    ontime_delivery_rate = (len(completed_orders_on_time)/len(completed_orders))*100
    related_vendor.on_time_delivery_rate = ontime_delivery_rate

    vms_logger.debug("this is the on time delivery date: ", ontime_delivery_rate)
    return ontime_delivery_rate

def calc_quality_rating_avg(related_vendor, quality_rating):
    #cache - store this data structure
    quality_rating_dict = {"bad":0, "below average":1, "average":2, "above average":3, "excellent":4}
    #cache - the sum of all ratings and *make changes acc
    all_orders = PurchaseOrder.objects.filter(vendor=related_vendor.id)
    ratings_record_list = [order.quality_rating for order in all_orders]
    average_value = sum(ratings_record_list)+quality_rating_dict[quality_rating]/len(ratings_record_list)
    related_vendor.quality_rating_avg = average_value
    return average_value




