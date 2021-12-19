from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models, transaction
from .models import User, Customer, Seller

class CustomerSignupForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    email=forms.EmailField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email=self.cleaned_data.get('email')
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.location=self.cleaned_data.get('location')
        customer.save()
        return user


class SellerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    phone=forms.CharField(required=True)
    licenseNumber=forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email=self.cleaned_data.get('email')
        user.is_seller = True
        user.save()
        seller=Seller.objects.create(user=user)
        seller.phone=self.cleaned_data.get('phone')
        seller.licenseNumber=self.cleaned_data.get('licenseNumber')
        seller.save()
        return seller

