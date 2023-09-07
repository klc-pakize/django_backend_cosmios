from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h2>MERAHA</h2>")

def haha(request):
    return HttpResponse("Hello Django")

def jajaj(request):
    return HttpResponse("Hello Django")

def jajajja(request):
    return HttpResponse("Hello Django")