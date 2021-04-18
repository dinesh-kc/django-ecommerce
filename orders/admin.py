from django.contrib import admin
from .models import CustomerOrder,Customer

from import_export import resources
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Customer)
@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    class Meta:
        pass


# class CustomerOrderResource(resources.ModelResource):
#     class Meta:
#         model = CustomerOrder
#         fields = ('quantity')
#         # fields = ['order_no','product_name','unit_price','quantity','total_price']



# class CustomerResourceAdmin(ImportExportModelAdmin):
#     resource_class = CustomerOrderResource

# admin.site.register(CustomerOrder, CustomerResourceAdmin)

@admin.register(CustomerOrder)
class CustomerOrderAdmin(ImportExportModelAdmin):
    list_display = ['order_no','product_name','unit_price','quantity','total_price','ordered_date']
    list_filter=('customer__name',)

    date_hierarchy = 'ordered_date'
    search_fields =  ('id','ordered_date')

    def has_add_permission(self, request, obj=None):
        return False
    
    def product_name(self,obj):
        return obj.product.name

    def order_no(self,obj):
        return f'#{obj.id}'
    
    def unit_price(self,obj):
        return obj.product.price
    
    def total_price(self,obj):
        return obj.product.price * obj.quantity