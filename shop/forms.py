from django import forms 
from .models import *

class FilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    