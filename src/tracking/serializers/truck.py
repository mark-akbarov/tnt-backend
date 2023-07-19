from rest_framework import serializers

from tracking.models.truck import TrailerIssue, TruckIssue
from tracking.utils.submit_issue import submit_truck_issue, submit_trailer_issue


class TruckIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckIssue
        fields = [
            'id',
            'issue',
            'status',
            'photos',
            'created_at',
        ]
        
    def create(self, validated_data):
        driver = self.context['request'].user
        submit_truck_issue(driver=driver, **validated_data)
        return validated_data



class TrailerIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrailerIssue
        fields = [
            'id',
            'issue',
            'status',
            'photos',
            'created_at',
        ]
        
    def create(self, validated_data):
        driver = self.context['request'].user
        submit_trailer_issue(driver=driver, **validated_data)
        return validated_data