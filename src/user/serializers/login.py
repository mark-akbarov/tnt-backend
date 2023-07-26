from rest_framework import serializers

from user.models.user import User
from user.utils.login import login


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
    
    def create(self, validated_data):
        login(**validated_data)
        return validated_data
