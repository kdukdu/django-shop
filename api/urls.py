from django.urls import path, include
from rest_framework import routers

from api.views import ProductViewSet, CategoryViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
