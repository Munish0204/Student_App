from django.db import models

class AttendanceTrend(models.Model):
    session = models.ForeignKey('awareness_sessions.Session', on_delete=models.CASCADE)
    date = models.DateField()
    attendance_count = models.IntegerField()

    class Meta:
        unique_together = ('session', 'date')

class StudentEngagement(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    session = models.ForeignKey('awareness_sessions.Session', on_delete=models.CASCADE)
    participation_status = models.BooleanField(default=False)
    points_earned = models.IntegerField(default=0)

    class Meta:
        unique_together = ('student', 'session')

class Report(models.Model):
    generated_at = models.DateTimeField(auto_now_add=True)
    report_type = models.CharField(max_length=100)
    data = models.JSONField()

    def __str__(self):
        return f"{self.report_type} Report - {self.generated_at}"