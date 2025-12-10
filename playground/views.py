from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItem 

# Create your views here.
def home(request):
    products = Product.objects.filter(inventory__lt=10)
    customers = Customer.objects.filter(email__icontains='.com')
    collections = Collection.objects.filter(featured_product__isnull=True)
    order = Order.objects.filter(customer__id=1)
    order_items = OrderItem.objects.filter(product__collection__id=3)
    context = {
        'products': products,
        'customers': customers,
        'collections': collections,
        'order': order,
        'order_items': order_items,
        'message': 'Welcome to the Storefront Playground!'
    }
    return render(request, 'hello.html', context)