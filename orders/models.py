from django.db import models
from vendors.models import Vendor
from django.core.exceptions import ValidationError
from django.utils import timezone
from model_utils import Choices

class PurchaseOrder(models.Model):
    STATUS = Choices("pending", "completed", "cancelled")

    RATING = Choices("bad", "below average", "average", "above average", "excellent")
    
    po_number = models.CharField(unique=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    delivery_date = models.DateTimeField(null=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS, default=STATUS.pending)
    quality_rating = models.FloatField(choices=RATING, null=True)
    issue_date = models.DateTimeField(null=True)
    acknowledgment_date = models.DateTimeField(null=True)

    def clean_quantity(value):
        if value < 1:
            raise ValidationError("You must order more than zilch products")
        