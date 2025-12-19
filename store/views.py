from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def product_list(request):
    return Response({"message": "List of products"})

@api_view(['GET'])
def product_detail(request, product_id):
    return Response({"message": f"Details of product {product_id}"})