from django.db import models

#from geoposition.fields import GeopositionField

# Create your models here.


class Buck(models.Model):
    image = models.ImageField(default=None, upload_to='./buckImages/')
    documents = models.FileField(default=None, blank=True, null=True, upload_to='documents/')
    weight = models.IntegerField(default=0)
    #location = GeopositionField()
    rackpoints = models.IntegerField(default=0)
    comments = models.ForeignKey('comments.Comment', default=None, on_delete=models.CASCADE, related_name="commentsAboutBuck")
    prize = models.IntegerField(default=0)
    user = models.ForeignKey('user_app.User', default=None, on_delete=models.CASCADE, related_name="userOwnedBuck")