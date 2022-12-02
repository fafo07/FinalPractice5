from xml.etree.ElementInclude import include
from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"Categorias", views.CatergoryViewSet)
router.register(r"Productos", views.ProductViewSet)
router.register(r"Proveedores", views.ProviderViewSet)
router.register(r"Almacenes", views.WarehouseViewSet)



urlpatterns = [
    path('Almacenes/listaproductos/<str:id>', views.Warehouse_Product_List),
    path('Almacenes/ProductosCantidadCero/<str:id>', views.Warehouse_Products_Quantity_Zero),
    path('Productos/CantidadCero/', views.Products_Quantity_Zero),
    path('',include(router.urls)),
]