from django.urls import path
from .views import IncreaseCreditAPI

urlpatterns = [
    path('sellers/<int:seller_id>/increase-credit/', IncreaseCreditAPI.as_view(), name='increase_credit'),
]
