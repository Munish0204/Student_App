from django.db import models
from awareness_sessions.models import AwarenessSession
from users.models import Student

class AttendanceAnalytics(models.Model):
    session = models.ForeignKey(AwarenessSession, on_delete=models.CASCADE, related_name='attendance_tracking_sessions')
    attendance_count = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.session.title} - {self.date}"

class EngagementAnalytics(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_engagements')
    session = models.ForeignKey(AwarenessSession, on_delete=models.CASCADE, related_name='attendance_engagement_sessions')
    engagement_score = models.FloatField()

    def __str__(self):
        return f"{self.student.user.username} - {self.session.title}"