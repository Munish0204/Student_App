from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Attendance
from .serializers import AttendanceSerializer
import qrcode
from django.http import HttpResponse

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @action(detail=True, methods=['get'])
    def generate_qr(self, request, pk=None):
        attendance = self.get_object()
        qr_code = qrcode.make(f'Attendance Code: {attendance.id}')
        response = HttpResponse(content_type='image/png')
        qr_code.save(response, 'PNG')
        return response

    @action(detail=True, methods=['post'])
    def mark_attendance(self, request, pk=None):
        student_id = request.data.get('student_id')
        attendance = self.get_object()
        attendance.mark_attendance(student_id)
        return Response({'status': 'attendance marked'})