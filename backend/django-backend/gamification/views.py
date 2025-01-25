from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Gamification
from .serializers import GamificationSerializer

class GamificationViewSet(viewsets.ModelViewSet):
    queryset = Gamification.objects.all()
    serializer_class = GamificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        gamification = self.get_object()
        serializer = self.get_serializer(gamification)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        gamification = self.get_object()
        serializer = self.get_serializer(gamification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        gamification = self.get_object()
        gamification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)