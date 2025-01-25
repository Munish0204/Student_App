from django.contrib import admin
from .models import AttendanceAnalytics, EngagementAnalytics

class AttendanceAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('session', 'attendance_rate', 'date')
    search_fields = ('session__title',)

class EngagementAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('student', 'participation_rate', 'session_count')
    search_fields = ('student__username',)

admin.site.register(AttendanceAnalytics, AttendanceAnalyticsAdmin)
admin.site.register(EngagementAnalytics, EngagementAnalyticsAdmin)