from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'message', 'status', 'created_at')
    search_fields = ('title', 'message')
    list_filter = ('status',)

admin.site.register(Notification, NotificationAdmin)