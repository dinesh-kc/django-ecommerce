from django.conf import settings 
from decimal import Decimal

from shop.models import Product

class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart
 

    def add(self,product,quantity):
        product_id = str(product.id)
        print(product_id)
        '''
        'product_cart":{
                '1': {'quantity:3,price:400},
                2: {'quantity:3,price:400},
                3: {'quantity:3,price:400},
                4: {'quantity:3,price:400},
            }
        '''
    
        if not product_id in self.cart:
            self.cart[product_id] = {'quantity':quantity,'price':str(product.price)}
        else:
      
            self.cart[product_id]['quantity'] += quantity
        self.save()
        
    def save(self):
        self.session.modified = True

# {'3': {'quantity': 1, 'price': '3455.00'}, '4': {'quantity': '111', 'price': '2800.00'}}

    def list(self):
        carts = []
        for product_id in self.cart.keys():
            obj = Product.objects.get(id=product_id)
            tmp_cart = {
                'id':product_id,
                'obj':obj,
                'quantity':self.cart[product_id]['quantity'],
                'price': Decimal(int(self.cart[product_id]['quantity']) * float(obj.price))
            }
            carts.append(tmp_cart)
        print("carts...")
        return carts

    def get_total_amount(self):
        return sum(float(v['price'])* int(v['quantity'] ) for v in self.cart.values())

        '''
        cart = {'3': {'quantity': 8.0, 'price': '3455.00'}}
        cart[3] = {'quantity': 8.0, 'price': '3455.00'}
        cart[3]['quantity'] = 8.0



        '''
    def update(self,quantity,product_id):
        pid = str(product_id)
        '''
dct = {'1':"idnesa','2':"dont knwo"}
dct['1'] = 'fjdsfk'
        '''
        # print(self.cart)s
        self.cart[pid]['quantity'] = quantity
        self.save()
        print(self.cart)

    def delete(self,product_id):
        pid = str(product_id)
        del self.cart[pid]
        self.save()

    def clearcart(self):
        del self.session[settings.CART_SESSION_KEY]
        self.save()

