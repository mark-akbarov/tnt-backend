from rest_framework import serializers

from tracking.models.truck import TrailerIssue, TruckIssue
from tracking.utils.submit_issue import submit_truck_issue, submit_trailer_issue


class TruckIssueCoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckIssue
        fields = [
            'id',
            'driver',
            'issue',
            'status',
            'photos',
            'created_at',
            'updated_at',
        ]


class TruckIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckIssue
        fields = [
            'id',
            'issue',
            'status',
            'photos',
            'created_at',
            'updated_at',
        ]
    
    def create(self, validated_data):
        user = self.context['request'].user
        submit_truck_issue(driver=user, **validated_data)
        return validated_data


class TrailerIssueCoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrailerIssue
        fields = [
            'id',
            'driver',
            'issue',
            'status',
            'photos',
            'created_at',
            'updated_at',
        ]


class TrailerIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrailerIssue
        fields = [
            'id',
            'issue',
            'status',
            'photos',
            'created_at',
            'updated_at',
        ]
    
    def create(self, validated_data):
        user = self.context['request'].user
        submit_trailer_issue(driver=user, **validated_data)        
        return validated_data
