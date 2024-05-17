from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import LivroViewSet

router = DefaultRouter()
router.register(r'books', LivroViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
