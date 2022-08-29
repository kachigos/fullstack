from rest_framework import generics
from rest_framework import permissions
from .models import Category
from .serializers import CategorySerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class Categories(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filter_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title', 'id']