from rest_framework import serializers
from .models import AttendanceAnalytics, EngagementAnalytics#, Report

class AttendanceAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceAnalytics
        fields = '__all__'

class EngagementAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementAnalytics
        fields = '__all__'

# class ReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Report
#         fields = '__all__'