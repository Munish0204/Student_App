from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('role', 'date_joined')
    ordering = ('-date_joined',)