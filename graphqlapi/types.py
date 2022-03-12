import graphene
from graphene_django import DjangoObjectType
from products.models import Product, Category, ProductCategory


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        exclude = []


class ProductCategoryType(DjangoObjectType):
    class Meta:
        model = ProductCategory
        exclude = []


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        exclude = []  # or fields = [...]

    currency_price = graphene.String()

    def resolve_currency_price(self, info):
        return '%.2f RON' % self.price

