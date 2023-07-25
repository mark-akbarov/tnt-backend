from rest_framework import serializers

from user.models.driver import Driver
from hometime.models.hometime import HomeTime
from hometime.utils.submit_request import submit_request


class HomeTimeCoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTime
        fields = [
            'id',
            'driver',
            'reason',
            'longitude',
            'latitude',
            'start_time',
            'return_time'
        ]
        

class HomeTimeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTime
        fields = [
            'id',
            'reason',
            'location_by_state',
            'status',
            'start_date',
            'return_date'
        ]
        
    def create(self, validated_data):
        driver = self.context['request'].user
        driver_instance = Driver.objects.filter(profile=driver).first()
        if driver_instance:
            submit_request(driver=driver_instance, **validated_data)
        else:
            raise serializers.ValidationError('You must be logged in as driver to perform this action.')
        return validated_data
