from django.db import models

from core.utils.base_model import BaseModel


class AccidentReportStatus(models.TextChoices):
    REPORTED =  'The accident has been reported to the relevant authorities or agency responsible for handling accident reports'
    UNDER_INVESTIGATION = 'The accident report is currently under investigation. This status indicates that authorities are collecting evidence, interviewing witnesses, and analyzing the circumstances of the accident'
    EVIDENCE_GATHERING = 'Investigators are in the process of gathering evidence, such as photographs, videos, witness statements, and other relevant information'
    INTERVIEWING_PARTIES = 'Authorities are conducting interviews with individuals involved in the accident, including drivers, passengers, and witnesses'
    PENDING_REVIEWS = 'The completed accident report is pending review by supervisory personnel or higher-ranking officers before being finalized'
    ACCIDENT_CAUSE_DETERMINED = 'Investigators have determined the primary cause of the accident based on evidence and statements gathered'
    FAULT_ASSIGNEMENT = 'If applicable, authorities have assigned fault or responsibility to one or more parties involved in the accident'
    PENDING_CHARGES = 'Law enforcement authorities are considering filing charges against individuals responsible for causing the accident due to violations of traffic laws or negligence'
    REPORT_COMPLETED = 'The accident report has been completed, including all necessary details, statements, and evidence. It is now ready for distribution or sharing with relevant parties'
    INSURANCE_CLAIM_FILED = 'If an insurance claim is related to the accident, this status indicates that the involved parties have filed their claims with their respective insurance companies'
    RESOLUTION_REACHED = 'The case has been resolved through negotiations, settlements, or other means. This status might indicate that the involved parties have agreed on a resolution outside of legal proceedings'
    LEGAL_ACTION_TAKEN = 'Legal action, such as a lawsuit, has been initiated as a result of the accident. This status indicates that the case has escalated beyond the investigative stage'
    CLOSED = 'The accident report has been closed, indicating that the investigation and any resulting actions or legal proceedings have been concluded'
    ARCHIVED = 'The accident report has been archived for future reference. This might happen after a certain period of time has passed since the accident'
    PENDING_UPDATES = 'The report is awaiting updates or additional information that may impact the conclusions or actions related to the accident'


class PoliceInvolmentStatus(models.TextChoices):
    NOT_NOTIFIED = 'No involvement of the law enforcement agencies'
    NOT_RESPONDED = 'Law enforcement was notified about the accident, but they did not respond to the scene (Minor Incident)'
    RESPONDED = 'Law enforcement authorities were notified about the accident and responded to the scene'
    INVESTIGATION_ONGOING = 'The police are actively investigating the accident'
    REPORT_FILED = 'After conducting a thorough investigation, the police have filed an official report detailing the accidents circumstances, parties involved, and their findings.'
    CLEARANCE_GIVEN = 'The police have concluded their investigation and given clearance for the involved vehicles to be moved from the accident scene'
    CHARGES_FILED = 'In cases where the accident was a result of a violation of traffic laws or negligence, the police may file charges against one or more parties involved'
    NO_POLICE_NEEDED = 'The parties involved exchanged information and resolved the situation amicably'
    UNKNOWN = 'The police involvement status is unknown or not disclosed in the available information'


class AccidentReport(BaseModel):
    driver = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='accident_reports')
    date = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    police_involvement = models.CharField(max_length=255, choices=PoliceInvolmentStatus.choices)
    report_status = models.CharField(max_length=255, choices=AccidentReportStatus.choices)
    
    class Meta:
        verbose_name = 'Accident Report'
        verbose_name_plural = 'Accident Reports'
    
    def __str__(self) -> str:
        return self.driver
