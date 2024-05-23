from rest_framework import serializers
from .models import PurchaseOrder
from vendors.serializers import VendorSerializer
import string
import random
from django.utils import timezone
from rest_framework.exceptions import ValidationError


class PurchaseOrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(required=False, allow_null=True) 
    issue_date = serializers.DateTimeField(required=False, allow_null=True)
    acknowledgment_date = serializers.DateTimeField(required=False, allow_null=True) 
    delivery_date = serializers.DateTimeField(required=False, allow_null=True)
    
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def create(self, validated_data):    
        
        if self.request.method=='POST':
            total = PurchaseOrder.objects.count()
            validated_data['po_number'] = total+1
    
            return PurchaseOrder.objects.create(**validated_data)
        else:
            pass
    
    def update(self, instance, validated_data):


        instance.po_number = validated_data.get('po_number', instance.po_number)
        instance.vendor = validated_data.get('vendor', instance.vendor)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.items = validated_data.get('items', instance.items)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.status = validated_data.get('status', instance.status)
        instance.quality_rating  =validated_data.get('quality_rating', instance.quality_rating)
        instance.issue_date = validated_data.get('issue_date', instance.issue_date)
        
        if instance.status == 'completed':
            instance.vendor.fulfillment_rate == 10

        instance.save()

        return instance
    
    def validate(self, date):
        
        if date['issue_date'] is not None:
            if date['order_date'] > date['issue_date']:
                print("order date locy")
                raise ValidationError("Issue date cannot preceed or overlap with order date")
        
        if date['acknowledgment_date'] and date['issue_date'] is not None:
            if date['issue_date'] >= date['acknowledgment_date']:
                raise ValidationError("Acknowledgement date cannot preceed the issue date")
        
        if date['acknowledgment_date'] and date['delivery_date'] is not None:
            if date['acknowledgment_date'] >= date['delivery_date']:
                raise ValidationError("Delivery date cannot preceed acknowledgement date")
            
        return date