from django.db import models

from core.utils.base_model import BaseModel
from tracking.models.issues import TrailerIssues, TruckIssues, IssueStatus


class TruckIssue(BaseModel):
    driver = models.ForeignKey('user.Driver', on_delete=models.CASCADE, related_name='truck_issues')
    issue = models.CharField(max_length=50, choices=TruckIssues.choices)
    status = models.CharField(max_length=50, choices=IssueStatus.choices, default=IssueStatus.OPEN)
    photos = models.ManyToManyField('file.File')
    
    class Meta:
        verbose_name = 'Truck Issue'
        verbose_name_plural = 'Truck Issues'

    def __str__(self) -> str:
        return str(self.id)
    

class TrailerIssue(BaseModel):
    driver = models.ForeignKey('user.Driver', on_delete=models.CASCADE, related_name='trailer_issues')
    issue = models.CharField(max_length=50, choices=TrailerIssues.choices)
    status = models.CharField(max_length=50, choices=IssueStatus.choices, default=IssueStatus.OPEN)
    photos = models.ManyToManyField('file.File')

    class Meta:
        verbose_name = 'Trailer Issue'
        verbose_name_plural = 'Trailer Issues'
        
    def __str__(self) -> str:
        return str(self.id)
