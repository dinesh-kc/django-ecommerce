from django.db import models
from shop.models import Product 

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='orders')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='total_orders')
    quantity = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-ordered_date',)
    
    