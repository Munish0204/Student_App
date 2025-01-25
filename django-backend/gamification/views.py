from rest_framework import generics
from .models import Gamification
from .serializers import GamificationSerializer

class GamificationListCreateView(generics.ListCreateAPIView):
    queryset = Gamification.objects.all()
    serializer_class = GamificationSerializer