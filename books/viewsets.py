from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer

class LivroPagination(PageNumberPagination):
    page_size = 5  

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    pagination_class = LivroPagination  
