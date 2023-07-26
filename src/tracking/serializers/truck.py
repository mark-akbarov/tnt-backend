from rest_framework import serializers

from tracking.models.truck import TrailerIssue, TruckIssue
from tracking.utils.submit_issue import submit_truck_issue, submit_trailer_issue
from user.models.user import User


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
        user = self.context['request'].user
        user_instance = User.objects.filter(profile=user).first()
        if user_instance:
            submit_truck_issue(driver=user_instance, **validated_data)
        else:
            raise serializers.ValidationError('You must be logged in as driver to perform this action.')
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
        user = self.context['request'].user
        user_instance = User.objects.filter(profile=user).first()
        if user_instance:
            submit_trailer_issue(driver=user, **validated_data)        
        else:
            raise serializers.ValidationError('You must be logged in to perform this action.')
        return validated_data
