from cart.cart import Cart


def cart_detail(request):
    cart = Cart(request)
    total_amount = cart.get_total_amount
    dct = {
        'total_amount':total_amount,
        'total_cart':len(cart.list())
    }
    return dct
