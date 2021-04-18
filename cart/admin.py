from django.contrib import admin
from django.contrib.auth.models import Group,User
from import_export import resources




admin.site.unregister(Group)
admin.site.unregister(User)


# Register your models here.
