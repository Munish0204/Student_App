from django.db import models
from awareness_sessions.models import AwarenessSession

class DigitalResource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('PDF', 'PDF'),
        ('Video', 'Video'),
        ('Infographic', 'Infographic'),
        ('Link', 'Link'),
    ]

    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    file_upload = models.FileField(upload_to='resources/')
    session = models.ForeignKey(AwarenessSession, related_name='resources', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.resource_type} - {self.session.title}"