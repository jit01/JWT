from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from jwtapp.models import userdetails
from jwtapp.serializer import jwtserializer


class UserView(generics.ListCreateAPIView):
    model=get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = userdetails.obeject.all()
    serializer_class = jwtserializer


####  To Display All Data present in userdetaisl

class Userdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = userdetails.obeject.all()
    serializer_class = jwtserializer

####  To Display The data according the PK value from userdetails data

class Detailstodo(generics.RetrieveUpdateDestroyAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = userdetails.obeject.all()
    serializer_class = jwtserializer
