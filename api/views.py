from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import *

# Create your views here.


class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
