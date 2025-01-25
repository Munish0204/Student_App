from django.urls import path
from . import views

urlpatterns = [
    path('generate-qr/<int:session_id>/', views.generate_qr_code, name='generate_qr_code'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance-report/<int:session_id>/', views.attendance_report, name='attendance_report'),
]