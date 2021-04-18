from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    class Meta:
        pass

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['image_tag','category_name','name','description','price','created','updated','available']
    

    def category_name(self,obj):
        return obj.category.name

    # def image_tag(self,obj):
    #     from django.utils.html import escape
    #     return u'<img src="%s" />' % escape(obj.image.url)
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True
