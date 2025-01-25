from rest_framework import serializers
from .models import AttendanceAnalytics, StudentEngagementAnalytics

class AttendanceAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceAnalytics
        fields = '__all__'

class StudentEngagementAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEngagementAnalytics
        fields = '__all__'