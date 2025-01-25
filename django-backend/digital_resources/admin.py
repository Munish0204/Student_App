from django.contrib import admin
from .models import DigitalResource

class DigitalResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'file']
    list_filter = []

admin.site.register(DigitalResource, DigitalResourceAdmin)