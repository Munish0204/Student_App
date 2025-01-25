from django.db import models
from users.models import User  # Assuming User model is in users app
from awareness_sessions.models import AwarenessSession  # Assuming AwarenessSession model is in awareness_sessions app

class Attendance(models.Model):
    session = models.ForeignKey(AwarenessSession, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session', 'student')

    def __str__(self):
        return f"{self.student.username} - {self.session.title} - {'Present' if self.attendance_status else 'Absent'}"