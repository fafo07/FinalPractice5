# Generated by Django 4.1.2 on 2022-10-07 23:01

from django.db import migrations, models
import warehouse.validators


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_product_category_product_description_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True, validators=[warehouse.validators.validate_no_empty_string]),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, validators=[warehouse.validators.validate_no_empty_string]),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True, validators=[warehouse.validators.validate_no_empty_string]),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, validators=[warehouse.validators.validate_not_negative_number]),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(null=True, validators=[warehouse.validators.validate_not_negative_number]),
        ),
        migrations.AlterField(
            model_name='provider',
            name='direction',
            field=models.CharField(max_length=100, null=True, validators=[warehouse.validators.validate_no_empty_string]),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True, validators=[warehouse.validators.validate_no_empty_string]),
        ),
        migrations.AlterField(
            model_name='provider',
            name='telephone',
            field=models.IntegerField(null=True, validators=[warehouse.validators.validate_not_negative_number]),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='direction',
            field=models.CharField(max_length=100, null=True, validators=[warehouse.validators.validate_no_empty_string]),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True, validators=[warehouse.validators.validate_no_empty_string]),
        ),
    ]
