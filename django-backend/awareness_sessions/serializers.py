from rest_framework import serializers
from .models import AwarenessSession

class AwarenessSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwarenessSession
        fields = ['id', 'title', 'description', 'date', 'time', 'venue', 'resources', 'categories', 'session_code']