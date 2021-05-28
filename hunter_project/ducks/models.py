from django.db import models

#from geoposition.fields import GeopositionField

# Create your models here.


class Duck(models.Model):
    image = models.ImageField(default=None, upload_to='duckImages/', null=True, blank=True)
    documents = models.FileField(default=None, blank=True, null=True, upload_to='documents/')
    weight = models.IntegerField(default=0)
    footsize = models.IntegerField(default=0)
    #location = GeopositionField()
    comments = models.ForeignKey('comments.Comment', default=None, on_delete=models.CASCADE, related_name="commentsAboutDuck")
    prize = models.IntegerField(default=0)
    user = models.ForeignKey('user_app.User', default=None, on_delete=models.CASCADE, related_name="userOwnedDuck")