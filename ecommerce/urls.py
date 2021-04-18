
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from shop.views import index

admin.site.site_header = 'Shop Ecommerce'
admin.site.site_title = 'Shop-ecommerce'
admin.site.index_title = 'shop-administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('order/',include('orders.urls')),
    path('cart/',include('cart.urls')),
    path('shop/',include('shop.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)