from django.contrib import admin
from alphaapp.models import seller, User, customer

# Register your models here.
admin.register(User)
admin.register(customer)
admin.register(seller)
