from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Departman, Personel
from .serializers import DepartmanSerializer, PersonelSerializer
from .permissions import IsAdminOrReadOnly

class DepartmanView(ListCreateAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class DepartmanDetail(RetrieveUpdateDestroyAPIView):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class PersonelView(ListCreateAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class PersonelDetail(RetrieveUpdateDestroyAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]