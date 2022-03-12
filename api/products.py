from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = []


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # pagination_class = ProductPaginator
