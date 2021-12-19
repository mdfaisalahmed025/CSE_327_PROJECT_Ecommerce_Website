from django import contrib
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractUser
from django.views.generic import CreateView
from django.http import HttpResponse
from django.contrib import messages
from .forms import CustomerSignupForm, SellerSignUpForm
from .models import User,Customer, Seller

# Create your views here.


def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def Signup(request):
    return render(request, 'register.html')


def log(request):
    """
    This method is used to view the login page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a search page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
          if request.method == 'POST':
              username =request.POST.get('guser_name')
              password =request.POST.get('guser_password')
             
              user= authenticate(request, username=username, password=password)

              if user is not None and user.is_guser:
                  login(request, user)
                  return redirect('home')
              elif user is not None and user.is_trainmaster:
                  messages.info(request, 'This  is for general users only, You are a Train Master')
              else:
                 messages.info(request, 'Username or Password is incorrect')
            
    context= {}
    return render(request, 'login.html', context)


def log2(request):
    """
    This method is used to view the login page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a search page which is a HTML page.
    :rtype: HttpResponse.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
          if request.method == 'POST':
              username =request.POST.get('seller_name')
              password =request.POST.get('seller_password')
             
              user= authenticate(request, username=username, password=password)

              if user is not None and user.is_seller:
                  login(request, user)
                  return redirect('home')
              elif user is not None and user.is_customer:
                  messages.info(request, 'This  is for Sellers only, You are a Customer')
              else:
                 messages.info(request, 'Username or Password is incorrect')
            
    context= {}
    return render(request, 'login2.html', context)


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignupForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class SellerSignupVIew(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('home')
   