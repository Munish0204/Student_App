from django.db import models
from django.utils import timezone

class AwarenessSession(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    resources = models.JSONField(blank=True, null=True)  # To store links, PDFs, etc.
    categories = models.CharField(max_length=255)  # Comma-separated categories
    session_code = models.CharField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date', 'time']