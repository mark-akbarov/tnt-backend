import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
    

class DriverType(models.TextChoices):
    SOLO = 'solo'
    TEAM = 'team'


class User(AbstractUser):
    username = models.CharField(max_length=255, default=uuid.uuid4, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    unit_id = models.CharField(max_length=100)
    vin_id = models.CharField(max_length=100)
    driver_type = models.CharField(max_length=10, choices=DriverType.choices, default=DriverType.SOLO)
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    profile_picture = models.OneToOneField('file.File', on_delete=models.CASCADE, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number', 'email', 'unit_id', 'vin_id']
    
    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"
