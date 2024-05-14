from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from datetime import datetime

class PurchaseOrderViewSet(ViewSet):

    authentication_classes = [TokenAuthentication]
    
    queryset = PurchaseOrder.objects.all()

    def list(self, request):
        serialized_obj = PurchaseOrderSerializer(self.queryset, many=True)
        return Response(serialized_obj.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):  
        item = get_object_or_404(self.queryset.all(), pk=pk)
        serialized_obj = PurchaseOrderSerializer(item)
        return Response(serialized_obj.data, status=status.HTTP_200_OK)
        
    def create(self, request):
        serialized_obj = PurchaseOrderSerializer(data=request.data)
        if serialized_obj.is_valid(raise_exception=True):
            serialized_obj.save()
            return Response(serialized_obj.data, status=status.HTTP_201_CREATED)
        return Response(serialized_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk):
        item = get_object_or_404(self.queryset, pk=pk)
        serialized_obj = PurchaseOrderSerializer(item, request.data, partial=True)
        if serialized_obj.is_valid(raise_exception=True):
            serialized_obj.save()
            return Response(serialized_obj.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
    def destroy(self, request, pk):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_200_OK)


class AcknowledgeOrderView(APIView):

    def patch(self, request, pk, date):
        instance = PurchaseOrder.objects.get(pk=pk)
        data = {"acknowledgement_data":datetime.now()}
        serialized_obj = PurchaseOrderSerializer(instance, data=data, partial=True)
        if serialized_obj.is_valid(raise_exception=True):
            serialized_obj.save()
            return Response(serialized_obj.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
