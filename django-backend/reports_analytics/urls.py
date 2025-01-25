from django.urls import path
from .views import AttendanceAnalyticsListCreateView, EngagementAnalyticsListCreateView #, ReportListCreateView

urlpatterns = [
    path('attendance/', AttendanceAnalyticsListCreateView.as_view(), name='attendance-analytics-list-create'),
    path('engagement/', EngagementAnalyticsListCreateView.as_view(), name='engagement-analytics-list-create'),
    # path('reports/', ReportListCreateView.as_view(), name='report-list-create'),
]