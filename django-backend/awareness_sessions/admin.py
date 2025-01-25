from django.contrib import admin
from .models import AwarenessSession

class AwarenessSessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'venue']
    list_filter = ['date']

admin.site.register(AwarenessSession, AwarenessSessionAdmin)