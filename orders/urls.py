from django.urls import path, include
from rest_framework import routers
from .views import *

app_label='orders'

router = routers.DefaultRouter()
router.register('', PurchaseOrderViewSet)

urlpatterns = [
    path('acknowledge/', AcknowledgeOrderView.as_view())
    ]
urlpatterns+=router.urls