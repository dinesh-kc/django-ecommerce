import requests
import json 

from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from shop.models import Product
from .cart import Cart

def cart_display(request):
	cart = Cart(request)
	carts = cart.list()
	context = {
		'cart':cart
	}
	return render(request,'cart.html',context)

	'''
[
   {
      "id":"3",
      "obj":"<Product":"Java Programming>",
      "quantity":8.0,
      "price":"Decimal("      "27640"      ")"
   },
   {
      "id":"2",
      "obj":"<Product":"Python Programming>",
      "quantity":1,
      "price":"Decimal("      "1500"      ")"
   },
   {
      "id":"1",
      "obj":"<Product":"Tshory>",
      "quantity":1,
      "price":"Decimal("      "500"      ")"
   }
]

	'''


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

def update_cart(request,id):
   if request.method == 'POST':
      data = request.POST
      quantity = data['quantity']
      cart = Cart(request)
      cart.update(quantity,id)

      context = {
            'cart':cart
         }

      return render(request,'cart.html',context)
def delete_cart(request,id):
   cart = Cart(request)
   cart.delete(id)
   context = {
            'cart':cart
         }
   return render(request,'cart.html',context)

@csrf_exempt
def verify_payment(request):
   data = request.POST
   product_id = data['product_identity']
   token = data['token']
   amount = data['amount']

   url = "https://khalti.com/api/v2/payment/verify/"
   payload = {
   "token": token,
   "amount": amount
   }
   headers = {
   "Authorization": "Key test_secret_key_c406db1d5d0e425a991d6de296d329e3"
   }
   

   response = requests.post(url, payload, headers = headers)
   
   response_data = json.loads(response.text)
   status_code = str(response.status_code)

   if status_code == '400':
      response = JsonResponse({'status':'false','message':response_data['detail']}, status=500)
      return response

   import pprint 
   pp = pprint.PrettyPrinter(indent=4)
   pp.pprint(response_data)
   
   return JsonResponse(f"Payment Done !! With IDX. {response_data['user']['idx']}",safe=False)
