from .serializers import (
    ProductSerializer,
    CosmeticCategorySerializer
)

from rest_framework import permissions, viewsets
from skin_care.models import (
    Product,
    CosmeticCategory
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class CosmeticCategoryViewSet(viewsets.ModelViewSet):
    queryset = CosmeticCategory.objects.all()
    serializer_class = CosmeticCategorySerializer
    permission_classes = [permissions.IsAuthenticated]