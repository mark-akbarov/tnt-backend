from rest_framework import generics
from rest_framework.permissions import AllowAny

from user.serializers.signup import SignupSerializer


class SignupAPIView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
