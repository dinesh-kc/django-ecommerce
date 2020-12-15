from django.urls import path 

from .views import *

urlpatterns = [
path('display',cart_display,name='cart_display'),
path('add_to_cart/<int:id>',add_to_cart,name='add_to_cart'),
path('update_cart/<int:id>',update_cart,name='update_cart'),
path('delete_cart/<int:id>',delete_cart,name='delete_cart'),

path('api/verify_payment',verify_payment,name='verify_payment')


]