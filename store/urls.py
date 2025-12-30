from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views
from pprint import pprint

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
products_router.register(r'reviews', views.ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + products_router.urls