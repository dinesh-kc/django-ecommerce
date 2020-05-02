from django.shortcuts import render
from .cart import Cart

def cart_display(request):
	return render(request,'cart.html')


def add_to_cart(request):
	cart = Cart(request)
	cart.save()
