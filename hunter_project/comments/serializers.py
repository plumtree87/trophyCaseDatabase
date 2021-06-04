from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'comment_text', 'original_comment',
                  'id', 'like', 'dislike', 'bass', 'duck', 'buck']