from django.shortcuts import render

from django.conf import settings

from .models import Product,Category
from .forms import *

def index(request):
    context  = {
        'products':Product.objects.all(),
        'form':FilterForm() 
        }
    
    return render(request,'index.html',context)