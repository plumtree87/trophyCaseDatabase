from rest_framework import serializers
from .models import Buck


class BuckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buck
        fields = [
            'image', 'documents',
            'weight', 'comments', 'prize', 'user', 'rackpoints', 'id', 'video_id'
        ]
