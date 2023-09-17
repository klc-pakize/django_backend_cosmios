from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer

# FBV
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# CBV
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet

#!#################### FUNCTION BASED VIEWS ########################################

@api_view()  # ['GET']
def home(request):
    return Response({
        "home":"Home Page"
    })
# http methods ----------->
# - GET (DB den veri çağırma, public)
# - POST(DB de değişklik, create, private)
# - PUT (DB DE KAYIT DEĞİŞKLİĞİ, private)
# - delete (dB de kayıt silme)
# - patch (kısmi update)

@api_view(['GET'])
def ogrencileri_listele(request):
    ogrenciler = Student.objects.all()  # students = Student.objects.all() 
    print(ogrenciler)
    queryset_data_json_cevir = StudentSerializer(ogrenciler, many=True)  # serializer = StudentSerializer(ogrenciler, many=True)
    print(queryset_data_json_cevir)
    return Response(queryset_data_json_cevir.data)  # return Response(serializer.data)


@api_view(['POST'])
def ogrenci_olustur(request):
    json_data_queryset_cevir = StudentSerializer(data=request.data)
    if json_data_queryset_cevir.is_valid():
        json_data_queryset_cevir.save()
        return Response(json_data_queryset_cevir.data, status=status.HTTP_201_CREATED)
    return Response(json_data_queryset_cevir.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ozel_ogrenci_detay_goruntuleme(request, pk):
    # try:
    #     ozel_ogrenci_queryset_datasi= Student.objects.get(id = pk)
    #     queryset_datami_json_data = StudentSerializer(ozel_ogrenci_queryset_datasi)
    # except:
    #     message = {
    #         "message":"Böyle bir öğrenci bulunmadı lütfen başka öğrenci id numarsını deneyin"
    #     }
    #     return Response(message)

    ozel_ogrenci_queryset_datasi = get_object_or_404(Student, id=pk)
    queryset_datami_json_data = StudentSerializer(ozel_ogrenci_queryset_datasi)
    return Response(queryset_datami_json_data.data)


@api_view(['PUT'])
def var_olan_ozel_obje_yenile(request, pk):
    eski_ognci_bilgi = get_object_or_404(Student, id=pk)
    json_data_artik_queryset = StudentSerializer(instance=eski_ognci_bilgi, data=request.data)
    if json_data_artik_queryset.is_valid():
        json_data_artik_queryset.save()
        mesaj = {
            "mesaj":"Öğrenci bilgi yenilendi"
        }
        return Response(mesaj)
    return Response(json_data_artik_queryset.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def ogrenc_sil(request, pk):
    silinecek_ogrenci_datasi = get_object_or_404(Student, id=pk)
    silinecek_ogrenci_datasi.delete()
    mesaj = {
        "mesaj":"Öğrenci başarılı bir şekilde silindi"
    }
    return Response(mesaj)
#!############################################################

#!#################### CLASS BASED VIEWS ########################################
class StudentListCreate(APIView):
    def get(self, request):
        ogrenciler = Student.objects.all()  # students = Student.objects.all() 
        print(ogrenciler)
        queryset_data_json_cevir = StudentSerializer(ogrenciler, many=True)  # serializer = StudentSerializer(ogrenciler, many=True)
        print(queryset_data_json_cevir)
        return Response(queryset_data_json_cevir.data)  # return Response(serializer.data)
    
    def post(self, request):
        json_data_queryset_cevir = StudentSerializer(data=request.data)
        if json_data_queryset_cevir.is_valid():
            json_data_queryset_cevir.save()
            return Response(json_data_queryset_cevir.data, status=status.HTTP_201_CREATED)
        return Response(json_data_queryset_cevir.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetail(APIView):

    def get(self, request, pk):
        ozel_ogrenci_queryset_datasi = get_object_or_404(Student, id=pk)
        queryset_datami_json_data = StudentSerializer(ozel_ogrenci_queryset_datasi)
        return Response(queryset_datami_json_data.data)
    
    def put(self, request, pk):
        eski_ognci_bilgi = get_object_or_404(Student, id=pk)
        json_data_artik_queryset = StudentSerializer(instance=eski_ognci_bilgi, data=request.data)
        if json_data_artik_queryset.is_valid():
            json_data_artik_queryset.save()
            mesaj = {
                "mesaj":"Öğrenci bilgi yenilendi"
            }
            return Response(mesaj)
        return Response(json_data_artik_queryset.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk):
        silinecek_ogrenci_datasi = get_object_or_404(Student, id=pk)
        silinecek_ogrenci_datasi.delete()
        mesaj = {
            "mesaj":"Öğrenci başarılı bir şekilde silindi"
        }
        return Response(mesaj)
    

#! GENERICAPIView and Mixins
""" #? GenericApıView
# One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

# GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views.

#? Mixins
# - ListModelMixin
#     - list method
# - CreateModelMixin
#     - create method
# - RetrieveModelMixin
#     - retrieve method
# - UpdateModelMixin
#     - update method
# - DestroyModelMixin
#     - destroy method 
    
"""

class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

#! Concrete Views

class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



#! ViewSets

# - Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. 

# - Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.

# There are two main advantages of using a ViewSet class over using a View class.

#  - Repeated logic can be combined into a single class. In the above example, we only need to specify the queryset once, and it'll be used across multiple views.
#  - By using routers, we no longer need to deal with wiring up the URL conf ourselves.

# Both of these come with a trade-off. Using regular views and URL confs is more explicit and gives you more control. ViewSets are helpful if you want to get up and running quickly, or when you have a large API and you want to enforce a consistent URL configuration throughout.


class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

#!############################################################