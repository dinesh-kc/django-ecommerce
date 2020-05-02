from django.contrib import admin

from .models import CustomerOrder,Customer

admin.site.register(Customer)

@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ['order_no','product_name','unit_price','quantity','total_price']
    list_filter=('customer__name',)
    
    def product_name(self,obj):
        return obj.product.name

    def order_no(self,obj):
        return f'#{obj.id}'
    
    def unit_price(self,obj):
        return obj.product.price
    
    def total_price(self,obj):
        return obj.product.price * obj.quantity