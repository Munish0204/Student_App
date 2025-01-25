from django.contrib import admin
from .models import Assignment

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'submission_type', 'deadline', 'evaluation_criteria')
    search_fields = ('title', 'description')
    list_filter = ('submission_type', 'deadline')