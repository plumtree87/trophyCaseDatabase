from rest_framework import serializers
from .models import Buck


class BuckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buck
        fields = [
            'imageUpload', 'documentsUpload', 'image', 'documents',
            'weight', 'comments', 'prize', 'user' 'rackpoints'
        ]