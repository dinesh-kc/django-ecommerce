from django.urls import path 

from .views import *

urlpatterns = [
path('product/<str:slug>',product_detail,name='product_detail'),
path('product_review/<int:product_id>',review_product,name='review_product')


]