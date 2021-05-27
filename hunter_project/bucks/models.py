from django.db import models

#from geoposition.fields import GeopositionField

# Create your models here.


class Buck(models.Model):
    imageUpload = models.ImageField(upload_to='uploads/', max_length=100)
    documentsUpload = models.FileField(upload_to='documentsUpload/', max_length=10000)
    image = models.ImageField()
    documents = models.FileField()
    weight = models.IntegerField(default=0)
    #location = GeopositionField()
    rackpoints = models.IntegerField(default=0)
    comments = models.ForeignKey('comments.Comment', default=None, on_delete=models.CASCADE, related_name="commentsAboutBuck")
    prize = models.IntegerField(default=0)
    user = models.ForeignKey('user_app.User', default=None, on_delete=models.CASCADE, related_name="userOwnedBuck")