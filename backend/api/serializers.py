from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
         #Fields to serialize when accepting and returning a user
        fields = ["id", "username", "password"]
        #Tells django to accept but DO NOT return password
        extra_kwargs = {"password": {"write_only": True}}

    #Method to create new user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"auther": {"read_only": True}}