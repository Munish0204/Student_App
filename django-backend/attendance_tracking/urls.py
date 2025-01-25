from django.urls import path
from .views import AttendanceViewSet

urlpatterns = [
    path('attendance-report/<int:session_id>/', AttendanceViewSet.as_view({'get': 'report'}), name='attendance_report'),
    path('generate-qr/<int:session_id>/', AttendanceViewSet.as_view({'get': 'generate_qr'}), name='generate_qr_code'),
    path('mark-attendance/', AttendanceViewSet.as_view({'post': 'mark_attendance'}), name='mark_attendance'),
]