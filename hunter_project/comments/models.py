from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.TextField(max_length=400)
