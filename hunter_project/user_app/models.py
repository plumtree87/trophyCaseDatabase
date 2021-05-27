from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.S


class User(AbstractUser):
    """Our custom user model that adds a new field to the default django user model"""


    def __str__(self):
        return self.username

