from django.db import models

from core.utils.base_model import BaseModel


class HomeTime(BaseModel):
    driver = models.ForeignKey('user.Driver', on_delete=models.CASCADE, related_name='hometime_requests')
    reason = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    return_date = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.driver}-from {self.start_date} to {self.return_date}"
