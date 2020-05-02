from django.shortcuts import render

def customer_order(request):
	return render(request,'orders.html')