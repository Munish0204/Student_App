from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('awareness-sessions/', include('awareness_sessions.urls')),
    path('attendance-tracking/', include('attendance_tracking.urls')),
    path('digital-resources/', include('digital_resources.urls')),
    path('interactive-assignments/', include('interactive_assignments.urls')),
    path('gamification/', include('gamification.urls')),
    path('notifications/', include('notifications.urls')),
    path('language-preferences/', include('language_preferences.urls')),
    path('reports-analytics/', include('reports_analytics.urls')),
    path('users/', include('users.urls')),
]