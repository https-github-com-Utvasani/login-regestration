from django import forms
from .models import Registration

class MyForm(forms.ModelForm):
  class Meta:
    model = Registration
    fields = ["username", "email","password"]
    labels = {'username': "username", "email": "email","password":"password"}