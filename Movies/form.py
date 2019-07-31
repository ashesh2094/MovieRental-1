from django import forms
from . import models

class addMovie(forms.ModelForm):
    class Meta:
        model = models.Movies
        fields= ['name','actor','year','genre','price']