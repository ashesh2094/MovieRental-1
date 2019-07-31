from django import forms
from . import models

class addCustomer(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields= ['name','age','city','zipcode','email']