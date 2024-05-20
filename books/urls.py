
from django.urls import path, include
from .views import BookList, UserCreate
from .viewsets import LivroViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', LivroViewSet)

urlpatterns = [
    path('api/books/', BookList.as_view(), name='book-list'),
    path('api/users/', UserCreate.as_view(), name='user-create'),
    path('api/', include(router.urls)), 
]
