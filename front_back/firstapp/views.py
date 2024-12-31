from django.shortcuts import render
# Create your views here.
from .serializers import SignUpSerializer
from django.contrib.auth.models import User
from rest_framework import generics


class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer