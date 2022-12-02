from django.contrib import admin
from .models import Category
from .models import Warehouse
from .models import Provider
from .models import Product

admin.site.register(Category)
admin.site.register(Warehouse)
admin.site.register(Provider)
admin.site.register(Product)