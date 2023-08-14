from rest_framework.viewsets import ModelViewSet

from tracking.models.accident import AccidentReport
from tracking.serializers.accident import AccidentReportSerializer


class AccidentReportViewSet(ModelViewSet):
    queryset = AccidentReport.objects.all()
    serializer_class = AccidentReportSerializer
