from django.shortcuts import render,redirect
from shop.models import Product
from .cart import Cart

def cart_display(request):
	cart = Cart(request)
	carts = cart.list()
	print(carts)
	return render(request,'cart.html')


def add_to_cart(request,id):
	if request.method == 'POST':
		print(request.session.get("product_cart"))
		product = Product.objects.get(id=id)
		quantity = request.POST['quantity']
		if not quantity:
			quantity = 1
		cart  = Cart(request)
		cart.add(product,quantity)
		# cart.add(product,quantity)
		return redirect('/')