from django.shortcuts import render

from django.conf import settings

from .models import Product,Category,ProductReview
from .forms import *

def index(request):
    context  = {
        'products':Product.objects.all(),
        'form':FilterForm(),
        'products_limited':Product.objects.all()[:4],
        
        }
    
    return render(request,'index.html',context)

def shop_page(request):
    context = {
        'products':Product.objects.all()
    }
    return render(request,'shop.html',context=context)

def product_detail(request,slug):
    product = Product.objects.filter(slug__icontains=slug)
    ft = request.GET.get('product_name')
    if ft:
        product = Product.objects.filter(name__icontains=ft)
    context = {}
    if product.exists():
        context['product'] = product.first()
        category = product.first().category
        reviews = ProductReview.objects.filter(product_id=product.first().id)
        print(reviews)
        context['reviews'] = reviews
        context['related_products'] = Product.objects.filter(category=category)
    return render(request,'product_detail.html',context=context)

def review_product(request,product_id):
    # pr = ProductReview.objects.create
    if request.method == 'POST':
        data = request.POST 
        name = data['name']
        review = data['review']
        ProductReview.objects.create(product_id=product_id,reviewed_by  =name,review=review)
    product = Product.objects.filter(id=product_id)
    context = {}
    ft = request.GET.get('product_name')
    if ft:
        product = Product.objects.filter(name__icontains=ft)
    if product.exists():
        context['product'] = product.first()
        category = product.first().category
        context['related_products'] = Product.objects.filter(category=category)
        reviews = ProductReview.objects.filter(product_id=product_id)
        print(reviews)
        context['reviews'] = reviews
    return render(request,'product_detail.html',context=context)

