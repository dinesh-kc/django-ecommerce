from django.urls import path 

from .views import *

urlpatterns = [
path('display',cart_display,name='cart_display'),
path('add_to_cart/<int:id>',add_to_cart,name='add_to_cart')

]