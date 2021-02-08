from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email",
                  "first_name", "last_name", "password"]

    def create(self, validated_data):
        user = super(UsersSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
