import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from file.models import File
    

class User(AbstractUser):
    username = models.CharField(max_length=255, default=uuid.uuid4, unique=True)
    unit_id = models.CharField(max_length=100)
    vin_id = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=255, null=True)
    longitude = models.CharField(max_length=255, null=True)
    profile_picture = models.OneToOneField(File, on_delete=models.CASCADE, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['unit_id', 'vin_id','phone_number', 'email']
    
    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"
