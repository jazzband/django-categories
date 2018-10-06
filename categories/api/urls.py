from rest_framework.routers import DefaultRouter

from .viewsets import CategoryViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, base_name='categories')
