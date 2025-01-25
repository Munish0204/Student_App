from django.contrib import admin
from .models import AttendanceAnalytics, EngagementAnalytics

class AttendanceAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['session', 'attendance_count', 'date']
    list_filter = ['date']

class EngagementAnalyticsAdmin(admin.ModelAdmin):
    list_display = ['student', 'session', 'engagement_score']
    list_filter = ['session']

admin.site.register(AttendanceAnalytics, AttendanceAnalyticsAdmin)
admin.site.register(EngagementAnalytics, EngagementAnalyticsAdmin)