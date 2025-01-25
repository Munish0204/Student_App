from django.contrib import admin
from .models import AwarenessSession

class AwarenessSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'venue', 'category')
    search_fields = ('title', 'description', 'category')
    list_filter = ('date', 'category')

admin.site.register(AwarenessSession, AwarenessSessionAdmin)