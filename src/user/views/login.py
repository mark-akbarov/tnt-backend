from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from user.serializers.login import LoginSerializer
from user.utils.login import login


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return login(**serializer.validated_data)
