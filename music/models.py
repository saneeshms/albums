from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist=models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})

    def __str__(self):
       return self.artist + '-' + self.album_title + '-' + self.genre +'-'+ self.logo.url

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=20)
    song_title=models.CharField(max_length=200)
    favorite=models.BooleanField(default=False)

    def __str__(self):
       return self.file_type+'-'+self.song_title
