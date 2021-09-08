from django.shortcuts import render
from rest_framework import generics, permissions

from .serializers import AccountRegistrationSerializer


class AccountRegistrationAPIView(generics.CreateAPIView):
    serializer_class = AccountRegistrationSerializer
    permission_classes = (permissions.AllowAny,)
