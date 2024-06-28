from django.urls import path, include
from .views import (
    ProductViewSet,
    CosmeticCategoryViewSet

)

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'cosmetics_categories', CosmeticCategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]