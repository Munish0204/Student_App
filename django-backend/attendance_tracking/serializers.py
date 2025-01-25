from rest_framework import serializers
from .models import AttendanceAnalytics

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceAnalytics
        fields = ['id', 'session', 'student', 'status', 'timestamp']  # Adjust fields as necessary

class AttendanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceAnalytics
        fields = ['session', 'student', 'status']  # Fields required for creating attendance records

class AttendanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceAnalytics
        fields = ['status']  # Fields that can be updated in attendance records