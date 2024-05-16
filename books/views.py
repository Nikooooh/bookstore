from rest_framework import generics
from .models import Livro
from .serializers import LivroSerializer

class BookList(generics.ListAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
