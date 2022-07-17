from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import Book
from rest_framework import viewsets

# Register serializer for labrarian
class RegisterSerializer_lab(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
     def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password']  ,is_staff=True)
        return user

# Register serializer for memeber
class RegisterSerializer_memeber(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
     def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')


# for add and edit books
class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name','author')


# book serializer for borrowing and returning book
class Bookserializers_member(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['status']


class Bookserializers_with_id(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','name','author')