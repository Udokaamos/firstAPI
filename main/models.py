from django.db import models
# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=50)
    publish_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
