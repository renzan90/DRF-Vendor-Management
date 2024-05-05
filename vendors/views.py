from django.shortcuts import render
from rest_framework.viewsets import Viewset
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

class VendorViewset(Viewset):

    queryset = Vendor.objects.all()

    def list(self, request):
        serialized = VendorSerializer(self.queryset, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        item = get_object_or_404(self.queryset, pk=pk)
        serialized = VendorSerializer(item)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serialized_obj = VendorSerializer(data=request.data)
        if serialized_obj.is_valid(raise_exception=True):
            serialized_obj.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        item = get_object_or_404(self.queryset, pk=pk)
        serialized_obj = VendorSerializer(item, request.data)
        if serialized_obj.is_valid(raise_exception=True):
            serialized_obj.save()
            return Response(data=serialized_obj.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        item = get_object_or_404(self.queryset, pk=pk)
        item.delete()
        return Response(status=status.HTTP_200_OK)