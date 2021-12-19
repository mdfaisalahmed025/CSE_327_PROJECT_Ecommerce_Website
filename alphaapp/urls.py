from django.urls import path
from . import views 
from .views import Signup, SellerSignupVIew, CustomerSignUpView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('signup', views.Signup, name='signup'),
    path('alphaapp/signup/customer/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('alphaapp/signup/seller/',   SellerSignupVIew.as_view(), name='seller_signup'),
]