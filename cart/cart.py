from django.conf import settings 

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
    def list(self):
        return self.cart
