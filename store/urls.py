from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'collections', views.CollectionViewSet)
router.register(r'carts', views.CartViewSet, basename='carts')

products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
products_router.register(r'reviews', views.ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-item-details')

urlpatterns = router.urls + products_router.urls + carts_router.urls