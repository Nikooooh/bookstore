
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Livro
from .serializers import LivroSerializer, UserSerializer
from rest_framework.permissions import AllowAny

class BookList(generics.ListAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  
