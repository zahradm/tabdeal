from django.urls import path
from .views import RechargeAPI

urlpatterns = [
    path('recharge/', RechargeAPI.as_view(), name='recharge_phone'),
]
