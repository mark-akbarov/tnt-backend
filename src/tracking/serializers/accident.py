from rest_framework import serializers

from tracking.models.accident import AccidentReport


class AccidentReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentReport
        fields = [
            'id',
            'driver',
            'description',
            'location',
            'police_involvement',
            'report_status',
        ]
