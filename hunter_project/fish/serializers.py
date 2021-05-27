from rest_framework import serializers
from .models import Bass

class BassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bass
        fields = [
            'imageUpload', 'documentsUpload', 'image', 'documents',
            'weight', 'comments', 'prize', 'user'
        ]
