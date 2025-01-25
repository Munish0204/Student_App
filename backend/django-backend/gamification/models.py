from django.db import models
from users.models import User

class Gamification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge_name = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    achievement_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.badge_name} - {self.points} points"