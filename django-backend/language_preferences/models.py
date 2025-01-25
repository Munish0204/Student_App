from django.db import models
from users.models import User

class LanguagePreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} - {self.language}"