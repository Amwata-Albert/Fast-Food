from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from .models import Profile,User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'roles')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
      user = User.objects.create_user(validated_data['username'], password = validated_data['password'], first_name=validated_data['first_name'], last_name=validated_data['last_name'], role=validated_data['roles'])
      return user
# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'\



# User serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  