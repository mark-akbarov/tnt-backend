from rest_framework import serializers

from user.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'unit_id',
            'vin_id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'profile_picture',
            ]
