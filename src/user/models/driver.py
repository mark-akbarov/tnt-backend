from django.db import models

from core.utils.base_model import BaseModel


class Driver(BaseModel):
    profile = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='drivers')
    unit_id = models.CharField(max_length=100)
    vin_id = models.CharField(max_length=100)
    
    REQUIRED_FIELDS = ['unit_id', 'vin_id']
    
    def __str__(self) -> str:
        return self.profile.username
