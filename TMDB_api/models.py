from django.db import models
# Create your models here.


class TMDB_Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField(null=True, blank=True)
    popularity = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    backdrop_path = models.CharField(max_length=500, null=True, blank=True)
    poster_path = models.CharField(max_length=500, null=True, blank=True)
    adult = models.BooleanField(default=False)
    overview = models.TextField()
    year = models.IntegerField()
    type = models.CharField(max_length=100)
    cast = models.TextField()
    character = models.TextField()
    director = models.CharField(max_length=255)

    def __str__(self):
        return self.title
