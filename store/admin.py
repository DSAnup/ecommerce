from django.contrib import admin
from .models import Product, Order, Collection

# Register your models here.
admin.site.register(Collection)
admin.site.register(Product)