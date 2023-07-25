from rest_framework.viewsets import ModelViewSet

from hometime.serializers.hometime import HomeTimeRequestSerializer
from hometime.models.hometime import HomeTime


class HomeTimeRequestViewSet(ModelViewSet):
    queryset = HomeTime.objects.all()
    serializer_class = HomeTimeRequestSerializer
