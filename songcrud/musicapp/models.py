from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400, null=True)
    age = models.IntegerField(null=True)
    
    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=400)
    date_released = models.DateTimeField(default=datetime.now, blank=True)
    #date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)  # --one artiste can have multiple song --one to many
    
    def __str__(self):
        return self.title
    


class Lyric(models.Model):
    content = models.CharField(max_length=400)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)  # --- one song can have multiple lyrics --- one to many
    def __str__(self):
        return self.content
    