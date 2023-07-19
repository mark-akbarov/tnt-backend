from django.db import models


class IssueType(models.TextChoices):
    TRUCK = 'Truck'
    TRAILER = 'Trailer'


class TruckIssues(models.TextChoices):
    ELECTRICAL_ISSUE = 'Electrical'
    FUEL_RELATED_ISSUE = 'Fuel Related'
    COOLING_SYSTEM_ISSUE = 'Cooling System'
    BRAKE_SYSTEM_ISSUE = 'Brake System'
    STEERING_AND_SUSPENSION_ISSUE = 'Steering and Suspension'
    OTHER = 'Other'
    

class TrailerIssues(models.TextChoices):
    FAULTY_LIGHING_ISSUE = 'Faulty Lighting Issue'
    TRAILER_COUPLING_FAILURE = 'Trailer Coupling Failure'
    CARGO_SECUREMENT_ISSUE = 'Cargo Securement'
    OTHER = 'Other'


class IssueStatus(models.TextChoices):
    OPEN = 'Open'
    IN_PROGRESS = 'In Progress'
    ON_HOLD = 'On Hold'
    FIXED = 'Fixed'
    NOT_FIXED = 'Not Fixed'
    PENDING_PARTS = 'Pending Parts'
    CLOSED = 'Closed'
    REOPENED = 'Reopened'
