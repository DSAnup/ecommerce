from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count, Func, F, Sum, Value, CharField, ExpressionWrapper, DecimalField, Min, Max, Avg
from django.db.models.functions import Concat
from store.models import Product, Customer, Collection, Order, OrderItem 

# Create your views here.
def home(request):
    ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    products = Product.objects.prefetch_related('promotions').select_related('collection').all()
    customers = Customer.objects.annotate(
        order_count=Count('order')
    )
    collections = Collection.objects.filter(featured_product__isnull=True)
    order = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # order_items = OrderItem.objects.all()
    orderhave = Order.objects.aggregate(
        total_items=Count('id')
    )
    product1 = OrderItem.objects.filter(product__id=1).aggregate(total_products=Sum('quantity'))
    customer1 = Order.objects.filter(customer__id=1).aggregate(
        total_orders=Count('id')
    )
    collection3 = Product.objects.filter(collection__id=3).annotate(
        min_price=Min('unit_price'), max_price=Max('unit_price'), avg_price=Avg('unit_price')
    )

    context = {
        'products': products,
        'customers': customers,
        'collections': collections,
        'orders': order,
        'orderhave': orderhave,
        'product1': product1,
        'customer1': customer1,
        'collection3': collection3,
        # 'order_items': order_items,
        'message': 'Welcome to the Storefront Playground!'
    }
    return render(request, 'hello.html', context)