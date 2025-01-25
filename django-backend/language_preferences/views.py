from rest_framework import generics
from .models import LanguagePreference
from .serializers import LanguagePreferenceSerializer

class LanguagePreferenceList(generics.ListCreateAPIView):
    queryset = LanguagePreference.objects.all()
    serializer_class = LanguagePreferenceSerializer

class LanguagePreferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LanguagePreference.objects.all()
    serializer_class = LanguagePreferenceSerializer