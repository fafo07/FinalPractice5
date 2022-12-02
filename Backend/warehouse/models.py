from enum import unique
from unicodedata import category, decimal
from unittest.util import _MAX_LENGTH
from django.db import models
from .validators  import validate_no_empty_string,validate_not_negative_number

class Category(models.Model):
    name = models.CharField(max_length=50, unique = True,null=True, validators=[validate_no_empty_string],)

class Provider(models.Model):
    name = models.CharField(max_length=50,unique=True,null=True,validators=[validate_no_empty_string],)
    telephone = models.IntegerField(null=True,validators=[validate_not_negative_number],)
    direction = models.CharField(max_length=100,null=True,validators=[validate_no_empty_string],)

class Warehouse(models.Model):
    name = models.CharField(max_length=50,unique=True,null=True,validators=[validate_no_empty_string],)
    direction = models.CharField(max_length=100,null=True,validators=[validate_no_empty_string],)

class Product(models.Model):
    name = models.CharField(max_length=50,unique=True,null=True,validators=[validate_no_empty_string],)
    description = models.TextField(null=True,validators=[validate_no_empty_string],)
    purchase_price = models.DecimalField(decimal_places=2,max_digits=10,null=True,validators=[validate_not_negative_number],)
    quantity = models.PositiveSmallIntegerField(null=True,validators=[validate_not_negative_number],)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    provider = models.ForeignKey(Provider,on_delete=models.CASCADE,null=True)
    warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE,null=True)
