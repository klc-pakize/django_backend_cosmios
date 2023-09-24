from django.urls import path, include

from rest_framework import routers

from .views import StudentMVS, PathMVS

router = routers.DefaultRouter()
router.register("stundetmvs", StudentMVS)  # stundent/ stundent/<int:pk>/ 
router.register("pathmvs", PathMVS)  # stundent/ stundent/<int:pk>/ 


urlpatterns = [


] + router.urls
