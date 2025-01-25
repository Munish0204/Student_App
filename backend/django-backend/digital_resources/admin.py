from django.contrib import admin
from .models import DigitalResource

class DigitalResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'session', 'uploaded_at')
    search_fields = ('title', 'resource_type')
    list_filter = ('resource_type', 'session')

admin.site.register(DigitalResource, DigitalResourceAdmin)