from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer
# Create your views here.

class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =  CategorySerializer
    filterset_fields = ["name"]

class BlogMVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filterset_fields = ["category__name"]
    search_fields = ['title', 'content']