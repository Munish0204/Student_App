from rest_framework import serializers
from .models import LanguagePreference

class LanguagePreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguagePreference
        fields = ['id', 'user_id', 'language']