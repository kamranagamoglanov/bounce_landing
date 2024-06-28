from rest_framework import serializers
from skin_care.models import (
    Product,
    CosmeticCategory
)


class CosmeticCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CosmeticCategory
        fields = (
            "id",
            "url",
            "title"
        )


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        fields = (
            "id",
            "url",
            "category",
            "name",
            "price",
            "production_date",
            "lifetime_in_days",
            "expired_at",
            "descriptions",
            "is_bestseller",
            "is_active",
        )
        