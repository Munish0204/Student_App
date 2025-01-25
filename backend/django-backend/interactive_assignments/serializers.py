from rest_framework import serializers
from .models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'submission_type', 'deadline', 'evaluation_criteria', 'created_at', 'updated_at']