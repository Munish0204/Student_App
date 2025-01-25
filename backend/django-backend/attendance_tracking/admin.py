from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('session', 'student', 'status', 'timestamp')
    search_fields = ('student__username', 'session__title')
    list_filter = ('status', 'session')
    ordering = ('-timestamp',)