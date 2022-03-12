from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=128, null=False)

class Product(models.Model):
    name = models.CharField(max_length=128, null=False)
    categories = models.ManyToManyField(Category, through='ProductCategory',related_name='products')
    quantity = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2) # minȘ 0.00
    color_gold = models.CharField(max_length=10, null=False)
    gramaj = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.IntegerField( default=0 , null=False )
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'<Product object ID = {self.name}>'

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='categories_pivot')  # product.categories[0].category.name
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_pivot')  # category.products[0].product.name
