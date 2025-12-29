from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from pprint import pprint

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'collections', views.CollectionViewSet)

urlpatterns = router.urls