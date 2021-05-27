from django.db import models

# Create your models here.


class Reply(models.Model):
    reply = models.TextField(max_length=400)
    user = models.ForeignKey('user_app.User', default=None, on_delete=models.CASCADE, related_name="repliesToComments")