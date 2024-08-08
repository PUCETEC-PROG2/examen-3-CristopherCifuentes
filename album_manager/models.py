from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title
