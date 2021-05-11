from django.forms import ModelForm
from django import forms
from .models import Order,Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']


