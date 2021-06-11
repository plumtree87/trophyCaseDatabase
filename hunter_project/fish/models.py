from django.db import models
from django.conf import settings
#from geoposition.fields import GeopositionField

# Create your models here.
def upload_to(instance, filename):
    return 'fishImages/{filename}'.format(filename=filename)

class Bass(models.Model):
    image = models.ImageField(default=None, upload_to=upload_to, null=True, blank=True)
    documents = models.FileField(default=None, blank=True, null=True, upload_to='fishDocuments/')
    weight = models.IntegerField(default=0)
    isPregnant = models.BooleanField(default=False)
    #location = GeopositionField()
    address = models.CharField(max_length=100, default=None)
    video_id = models.CharField(max_length=50, default=None)
    comments = models.ForeignKey('comments.Comment', default=None, blank=True, null=True, on_delete=models.CASCADE, related_name="commentsAboutBass")
    prize = models.IntegerField(default=0)
    user = models.ForeignKey('user_app.User', default=None, on_delete=models.CASCADE, related_name="userOwnedBass")