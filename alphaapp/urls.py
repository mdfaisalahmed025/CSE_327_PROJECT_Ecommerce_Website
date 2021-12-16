from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('login/', views.login, name='login')   
]