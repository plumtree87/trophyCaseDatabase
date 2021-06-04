from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_text = models.TextField(max_length=1000, blank=True)
    user = models.ForeignKey('user_app.User', default=None, on_delete=models.CASCADE, related_name="userOwnedComment")
    buck = models.ForeignKey('bucks.Buck', on_delete=models.CASCADE, null=True, blank=True, related_name="buckCommentedOn")
    duck = models.ForeignKey('ducks.Duck', on_delete=models.CASCADE, null=True, blank=True, related_name="duckCommentedOn")
    bass = models.ForeignKey('fish.Bass', on_delete=models.CASCADE, null=True, blank=True, related_name="bassCommentedOn")
    original_comment = models.ForeignKey('comments.Comment', blank=True, null=True, on_delete=models.CASCADE, related_name="commentCommentedOn")
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
