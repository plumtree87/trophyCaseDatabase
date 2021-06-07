from rest_framework import serializers
from .models import Bass

class BassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bass
        fields = [
            'image', 'documents',
            'weight', 'comments', 'prize', 'user', 'isPregnant', 'id', 'video_id'
        ]
