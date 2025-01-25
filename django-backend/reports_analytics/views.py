from rest_framework import generics
from .models import AttendanceAnalytics, EngagementAnalytics
from .serializers import AttendanceAnalyticsSerializer, EngagementAnalyticsSerializer#

class AttendanceAnalyticsListCreateView(generics.ListCreateAPIView):
    queryset = AttendanceAnalytics.objects.all()
    serializer_class = AttendanceAnalyticsSerializer

class EngagementAnalyticsListCreateView(generics.ListCreateAPIView):
    queryset = EngagementAnalytics.objects.all()
    serializer_class = EngagementAnalyticsSerializer

