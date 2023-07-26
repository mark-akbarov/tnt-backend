from rest_framework import serializers

from user.models.user import User
from user.utils.signup import signup


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'unit_id',
            'vin_id',
            'password'
        ]       
    
    def create(self, validated_data):
        signup(**validated_data)
        return validated_data
