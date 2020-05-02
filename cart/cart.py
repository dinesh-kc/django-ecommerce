from django.conf import settings 
class Cart(object):
    def __init__(self):
        print("reacched here ")
        self.cart = self.request.session 

        print(self.cart)

    def save():
        print("saved")