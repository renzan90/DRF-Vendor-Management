from django.db import models
from vendors.models import Vendor
from django.core.exceptions import ValidationError
from django.utils import timezone

class PurchaseOrder(models.Model):
    STATUS = {
        "P":"pending",
        "CO":"completed",
        "CA":"cancelled",
    }

    RATING = {
        "ONE":"bad",
        "TWO":"below average",
        "THREE":"average",
        "FOUR":"above average",
        "FIVE":"excellent"
    }
    po_number = models.CharField(unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS, default=STATUS[0])
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
        