from django.urls import path

from .views import home, ogrencileri_listele, ogrenci_olustur, ozel_ogrenci_detay_goruntuleme, var_olan_ozel_obje_yenile, ogrenc_sil

urlpatterns = [
    path("home/", home),
    path("students/", ogrencileri_listele),
    path("students/create/", ogrenci_olustur),
    path("students/<int:pk>/", ozel_ogrenci_detay_goruntuleme),
    path("student/update/<int:pk>/", var_olan_ozel_obje_yenile),
    path("student/delete/<int:pk>/", ogrenc_sil),
]
