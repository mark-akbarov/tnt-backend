from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from user.serializers.signup import SignupSerializer
from user.utils.signup import signup


class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return signup(**serializer.validated_data)
