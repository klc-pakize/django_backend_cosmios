from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User



class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required = True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True, required = True)
    first_name = serializers.CharField(required = True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
            'password2',
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password":"Password fields didn't match!!!"
            })
        return attrs
    
    def create(self, validated_data):
       user = User.objects.create(
           username = validated_data['username'],
           email = validated_data['email'],
           first_name = validated_data['first_name'],
           last_name = validated_data['last_name']
       )

       user.set_password(validated_data['password'])
       user.save()

       return user