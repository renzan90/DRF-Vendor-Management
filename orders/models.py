from django.db import models
from vendors.models import Vendor
from django.core.exceptions import ValidationError
from django.utils import timezone
from model_utils import Choices

class PurchaseOrder(models.Model):
    STATUS = Choices("pending", "completed", "cancelled")

    RATING = Choices("bad", "below average", "average", "above average", "excellent")
    
    po_number = models.CharField(unique=True, default=None)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS, default=STATUS.pending)
    quality_rating = models.FloatField(choices=RATING, null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def clean(self):
        assert self.order_date < self.issue_date, \
        "Issue date cannot preceed or overlap with order date"
        
        assert self.issue_date <= self.acknowledgment_date, \
        "Acknowledgement date cannot preceed the issue date"

        assert self.acknowledgment_date <= self.delivery_date, \
        "Delivery date cannot preceed acknowledgement date"

    def clean_quantity(value):
        if value < 0:
            raise ValidationError("You must order more than zilch products")
        