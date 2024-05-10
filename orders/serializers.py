from rest_framework import serializers
from .models import PurchaseOrder
import string
import random
from django.utils import timezone


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'PurchaseOrder'
        fields = '__all__'

    def create(self, validated_data):
        digits = string.digits

        validated_data['po_number'] = 'po-'+''.join(random.choices(digits, k=5))

        return PurchaseOrder.objects.create(**validated_data)
    
    def update(self, validated_data):

        if validated_data['status'] == 'completed':
            self.real_delivery_date = timezone.now()
