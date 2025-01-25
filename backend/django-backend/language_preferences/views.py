from rest_framework import viewsets
from rest_framework.response import Response
from .models import LanguagePreference
from .serializers import LanguagePreferenceSerializer

class LanguagePreferenceViewSet(viewsets.ModelViewSet):
    queryset = LanguagePreference.objects.all()
    serializer_class = LanguagePreferenceSerializer

    def get_user_language(self, request):
        user_id = request.user.id
        language_preference = self.queryset.filter(user_id=user_id).first()
        if language_preference:
            return Response({'language': language_preference.language})
        return Response({'language': None})

    def set_user_language(self, request):
        user_id = request.user.id
        language = request.data.get('language')
        language_preference, created = LanguagePreference.objects.update_or_create(
            user_id=user_id,
            defaults={'language': language}
        )
        return Response({'language': language_preference.language})