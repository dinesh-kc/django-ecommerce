from django.urls import path 
from .views import *

app_name = 'orders'

urlpatterns = [
    path('',customer_order,name='order'),
    # path('checkout_successful/',checkout_successful,name='checkout_successful')
]