from rest_framework.permissions import AllowAny
from rest_framework import generics

from user.serializers.login import LoginSerializer


class LoginAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
