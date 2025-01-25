from rest_framework import serializers
from .models import DigitalResource

class DigitalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalResource
        fields = ['id', 'resource_type', 'file_upload', 'associated_session']