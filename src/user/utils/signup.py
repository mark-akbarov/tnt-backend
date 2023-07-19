from rest_framework.response import Response
from rest_framework import status

from user.models.base import User
from user.utils.verification import send_user_verify_code


def signup(username: str, email: str, phone_number: str, unit_id: str, vin_id:str, password):
    check_email = User.objects.filter(email=email, is_active=True).exists()
    if check_email is True:
        return Response({'type': 'E_EMAIL_EXISTS', 'message': 'Email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    user = create_user(
        username=username,
        email=email,
        phone_number=phone_number,
        unit_id=unit_id,
        vin_id=vin_id,
        password=password
    )
    send_user_verify_code(user)
    return Response({'message': 'Successfully registered'}, status=status.HTTP_201_CREATED)


def create_user(
        username: str,
        email: str,
        phone_number: str,
        unit_id: str,
        vin_id: str,
        password=None
):
    user = User.objects.create(
        username=username,
        email=email,
        phone_number=phone_number,
        unit_id=unit_id,
        vin_id=vin_id,
        is_active=False,
        is_staff=False,
        is_superuser=False,
    )
    if password:
        user.set_password(password)
        user.save()
    return user
