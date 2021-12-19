from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.db import models, transaction
from django.forms import ModelForm, fields

from .models import User, customer, Seller

class CustomerSignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User


class SellerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phone=forms.CharField(required=True)
    licenseNumber=forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

