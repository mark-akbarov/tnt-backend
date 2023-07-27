from rest_framework import serializers


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()
    unit_id = serializers.CharField()
    vin_id = serializers.CharField()
    password = serializers.CharField()
