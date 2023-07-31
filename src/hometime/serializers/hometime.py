from rest_framework import serializers

from user.serializers.user import UserSerializer
from hometime.models.hometime import HomeTime
from hometime.utils.submit_request import submit_request


class HomeTimeCoreSerializer(serializers.ModelSerializer):
    driver = UserSerializer()
    
    class Meta:
        model = HomeTime
        fields = [
            'id',
            'driver',
            'reason',
            'location_by_state',
            'start_date',
            'return_date',
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
