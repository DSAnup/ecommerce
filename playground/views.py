from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItem 

# Create your views here.
def home(request):
    products = Product.objects.prefetch_related('promotions').select_related('collection').all()
    customers = Customer.objects.filter(email__icontains='.com')
    collections = Collection.objects.filter(featured_product__isnull=True)
    order = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # order_items = OrderItem.objects.all()

    context = {
        'products': products,
        'customers': customers,
        'collections': collections,
        'orders': order,
        # 'order_items': order_items,
        'message': 'Welcome to the Storefront Playground!'
    }
    return render(request, 'hello.html', context)