from django.contrib import admin
from django.urls import path
from jwtapp.views import UserView,Userdetails,Detailstodo

urlpatterns = [
    path('',UserView.as_view()),
    path('<int:pk>',Userdetails.as_view())
]