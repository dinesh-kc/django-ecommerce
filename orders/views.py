from django.shortcuts import render,get_object_or_404,redirect
from .forms import *
from django.urls import reverse
from cart.cart import Cart
from django.http import HttpResponse
from decimal import Decimal

from django.core.files.storage import FileSystemStorage
from weasyprint import HTML
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail,EmailMessage

def html_to_pdf_view(request,customer_id):
    customer = CustomerOrder.objects.filter(customer_id=customer_id)
    html_string = render_to_string('invoice.html', {
                                'orders': customer,
                                'order_no':customer[0].id,
                                'total_amount': sum([Decimal(item.quantity * item.product.price) for item in customer])
                                })
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()
    
    email =EmailMessage(
        'Order Invoice',
        'Dear {0} Your order is placed successfully. Here is the order detail'.format(customer[0].customer.name),
        settings.EMAIL_HOST_USER,
        [customer[0].customer.email],
      
        )
    email.attach('invoice.pdf',pdf_file)
    email.send(fail_silently=False)
    print("email send")
    
    return render(request,'checkout_successful.html',{'order_id':customer[0].id})
    

def customer_order(request):
    if request.method == 'POST':
        form = BillingModelForm(request.POST)
        if form.is_valid():
            cart = Cart(request)
            customer = form.save()
            total_carts = cart.list()
            for c in total_carts:
                obj,created =  CustomerOrder.objects.get_or_create(
                    customer=customer,
                    defaults = {
                        'product':c['obj'],
                        'quantity':c['quantity']
                        }
                    )
            if obj:
                cart.clearcart()
                # html_to_pdf_view(obj.id)
                return redirect(reverse('orders:invoice',args=[customer.id]))
                
    form = BillingModelForm()
    
    context = {
        'form':form,
        'cart':Cart(request)
    }
    return render(request,'orders.html',context)

def checkout_successful(request):
    return render(request,'checkout_successful.html')

