from django.urls import path, include

from .views import DepartmanView, PersonelView, PersonelDetail, DepartmanDetail


urlpatterns = [
    path("departmans/", DepartmanView.as_view()),
    path("personels/", PersonelView.as_view()),
    path("personels/<int:pk>/", PersonelDetail.as_view()),
    path("departmans/<int:pk>/", DepartmanDetail.as_view()),
]