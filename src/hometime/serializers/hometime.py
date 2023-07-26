from rest_framework import serializers

from user.models.user import User
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
        user = self.context['request'].user
        submit_request(driver=user, **validated_data)
        return validated_data
