from rest_framework import serializers
from .models import Vendor
import string
import random

class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = '__all__'

    def create(self, validated_data):
        ascii = string.ascii_uppercase
        digits = string.digits

        complete_code = ascii + digits

        validated_data['vendor_code'] = ''.join(random.choices(complete_code, k=5))

        validated_data['on_time_delivery_rate'] = None
        validated_data['quality_rating_avg'] = None
        validated_data['average_response_time'] = None
        validated_data['fulfillment_rate'] = None

        return Vendor.objects.create(**validated_data)

