from django.db import models
from vendors.models import Vendor

class PurchaseOrder(models.Model):
    STATUS = {
        "P":"pending",
        "CO":"completed",
        "CA":"cancelled",
    }
    po_number = models.CharField(unique=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)
