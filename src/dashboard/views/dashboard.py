from rest_framework import generics

from dashboard.models import  (
    HomeTime,
    TrailerIssue,
    TruckIssue
    )

from dashboard.serializers import (
    TrailerIssueCoreSerializer, 
    TruckIssueCoreSerializer, 
    HomeTimeCoreSerializer
    )


class HomeTimeDashboardListView(generics.ListAPIView):
    queryset = HomeTime.objects.all()
    serializer_class = HomeTimeCoreSerializer


class TruckIssueDashboardListView(generics.ListAPIView):
    queryset = TruckIssue.objects.all()
    serializer_class = TruckIssueCoreSerializer


class TrailerIssueDashboardListView(generics.ListAPIView):
    queryset = TrailerIssue.objects.all()
    serializer_class = TrailerIssueCoreSerializer
