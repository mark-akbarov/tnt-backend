from rest_framework import serializers

from user.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'phone_number',
            'email',
            'first_name',
            'last_name',
            'unit_id',
            'vin_id',
            'driver_type',
            'profile_picture',
            ]
