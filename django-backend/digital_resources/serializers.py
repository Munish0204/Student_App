from rest_framework import serializers
from .models import DigitalResource

class DigitalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalResource
        fields = '__all__'