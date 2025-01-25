from django.db import models
from awareness_sessions.models import AwarenessSession

class DigitalResource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='digital_resources/')
    session = models.ForeignKey(AwarenessSession, on_delete=models.CASCADE, related_name='digital_resources')

    def __str__(self):
        return self.title