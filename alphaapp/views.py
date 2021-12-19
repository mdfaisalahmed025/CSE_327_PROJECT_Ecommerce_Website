from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import CreateView
from django.http import HttpResponse
from .forms import CustomerSignupForm, SellerSignUpForm
from .models import User, customer, seller

# Create your views here.
def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def Signup(request):
    return render(request, 'signup.html')


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignupForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'guser'
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
        kwargs['user_type'] = 'trainmaster'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('home')
   