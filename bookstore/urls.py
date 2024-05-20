
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as drf_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('books.urls')),
    path('api-token-auth/', drf_views.obtain_auth_token, name='api_token_auth'),  
]
