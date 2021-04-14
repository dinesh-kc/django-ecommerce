from django import forms 

from .models import *


class BillingModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'