from rest_framework import serializers

from tracking.models.truck import TrailerIssue, TruckIssue
from tracking.utils.submit_issue import submit_truck_issue, submit_trailer_issue
from user.models.driver import Driver


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
        driver_instance = Driver.objects.filter(profile=driver).first()
        if driver_instance:
            submit_truck_issue(driver=driver_instance, **validated_data)
        else:
            raise serializers.ValidationError('You must logged in as driver to perform this action.')
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
        driver_instance = Driver.objects.filter(profile=driver).first()
        if driver_instance:
            submit_trailer_issue(driver=driver, **validated_data)        
        else:
            raise serializers.ValidationError('You must logged in as driver to perform this action.')
        return validated_data
