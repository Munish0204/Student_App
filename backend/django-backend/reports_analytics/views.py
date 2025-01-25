from rest_framework import viewsets
from rest_framework.response import Response
from .models import AttendanceAnalytics, EngagementAnalytics
from .serializers import AttendanceAnalyticsSerializer, EngagementAnalyticsSerializer

class AttendanceAnalyticsViewSet(viewsets.ViewSet):
    def list(self, request):
        analytics = AttendanceAnalytics.objects.all()
        serializer = AttendanceAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data)

class EngagementAnalyticsViewSet(viewsets.ViewSet):
    def list(self, request):
        analytics = EngagementAnalytics.objects.all()
        serializer = EngagementAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data)