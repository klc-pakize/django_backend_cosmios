from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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