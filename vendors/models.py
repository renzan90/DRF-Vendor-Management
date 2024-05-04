from django.db import models
import string
import random

class Vendor(models.Model):
    name = models.CharField(max_length=20)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True, null=True)
    on_time_delivery_rate = models.FloatField(blank=True, null=True)
    quality_rating_avg = models.FloatField(blank=True, null=True)
    average_response_time = models.FloatField(blank=True, null=True)
    fulfillment_rate = models.FloatField(blank=True, null=True)

    def save(self):
        ascii = string.ascii_uppercase
        digits = string.digits

        complete_code = ascii + digits

        self.vendor_code = ''.join(random.choices(complete_code, k=5))

        super().save()
