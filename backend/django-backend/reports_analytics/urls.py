from django.urls import path
from . import views

urlpatterns = [
    path('attendance-analytics/', views.AttendanceAnalyticsView.as_view(), name='attendance_analytics'),
    path('student-engagement/', views.StudentEngagementView.as_view(), name='student_engagement'),
    path('export-report/', views.ExportReportView.as_view(), name='export_report'),
]