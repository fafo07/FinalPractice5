from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import Category , Product, Provider, Warehouse
from .serializers import CategorySerializer,ProductSerializer,ProviderSerializer,WarehouseSerializer


class CatergoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer

class ProviderViewSet(viewsets.ModelViewSet):
    queryset= Provider.objects.all()
    serializer_class = ProviderSerializer

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset= Warehouse.objects.all()
    serializer_class = WarehouseSerializer

@api_view(["GET"])
def Warehouse_Product_List(request, id):
    """
    Lista de productos por Almacen
    """
    try:
        ProductList = Product.objects.filter(warehouse_id = id)
        return JsonResponse(
            ProductSerializer(ProductList, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)

@api_view(["GET"])
def Warehouse_Products_Quantity_Zero(request,id):
    """
    Lista de productos con cantidad 0 en almacen
    """
    try:
        ProductList = Product.objects.filter(warehouse_id = id, quantity = 0)
        return JsonResponse(
            ProductSerializer(ProductList, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


@api_view(["GET"])
def Products_Quantity_Zero(request):
    """
    Lista de productos con cantidad 0
    """
    try:
        ProductList = Product.objects.filter(quantity = 0)
        return JsonResponse(
            ProductSerializer(ProductList, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)