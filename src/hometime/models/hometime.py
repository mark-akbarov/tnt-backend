from django.db import models

from core.utils.base_model import BaseModel


class RequestStatus(models.TextChoices):
    WAITING_FOR_APPROVAL = 'Waiting for Approval'
    APPROVED = 'Approved'
    

class Reason(models.TextChoices):
    HOS = "Regulated Hours of Service"
    HEALTH_ISSUES = "Health Related Issues"
    FAMILY_EMERGENCY = "Family Emergency"
    OTHER = "Other Reasons"


class HomeTime(BaseModel):
    driver = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='hometime_requests')
    reason = models.CharField(max_length=255, choices=Reason.choices, default=Reason.HOS)
    status = models.CharField(max_length=50, choices=RequestStatus.choices, default=RequestStatus.WAITING_FOR_APPROVAL)
    location_by_state = models.CharField(max_length=255)
    longitude = models.CharField(max_length=25)
    latitude = models.CharField(max_length=25)
    start_date = models.DateField()
    return_date = models.DateField()
    
    def __str__(self) -> str:
        return f"{self.driver} - from {self.start_date} -> {self.return_date}"
