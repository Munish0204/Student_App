from django.contrib import admin
from .models import Gamification

@admin.register(Gamification)
class GamificationAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'badge_name', 'points', 'achievement_date')
    search_fields = ('user_id', 'badge_name')
    list_filter = ('achievement_date',)