from django.shortcuts import render

from .serializers import RegisterSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User


# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     print(response.data)
    #     token = Token.objects.create(user_id = response.data['id'])
    #     response.data['token'] = token.key
    #     return response


# ----------- User Logout Function ------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Kullanıcı Çıkış (Token Sil)
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})