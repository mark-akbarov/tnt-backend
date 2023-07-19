from rest_framework.viewsets import ModelViewSet

from tracking.serializers.truck import TruckIssueSerializer, TrailerIssueSerializer
from tracking.models.truck import TruckIssue, TrailerIssue


class TruckIssueModelViewSet(ModelViewSet):
   queryset = TruckIssue.objects.all()
   serializer_class = TruckIssueSerializer


class TrailerIssueModelViewSet(ModelViewSet):
   queryset = TrailerIssue.objects.all()
   serializer_class = TrailerIssueSerializer
