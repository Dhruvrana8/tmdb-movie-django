from django.db import models
# Create your models here.


class TMDB_Movies(models.Model):
    title = models.CharField(max_length=255)
    vote_average = models.DecimalField(max_digits=3, decimal_places=2)
    vote_count = models.IntegerField()
    status = models.CharField(max_length=100)
    release_date = models.DateField()
    revenue = models.BigIntegerField()
    runtime = models.IntegerField()
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=255)
    budget = models.BigIntegerField()
    homepage = models.URLField()
    imdb_id = models.CharField(max_length=15)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=255)
    overview = models.TextField()
    popularity = models.DecimalField(max_digits=5, decimal_places=2)
    poster_path = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    production_companies = models.CharField(max_length=255)
    production_countries = models.CharField(max_length=255)
    spoken_languages = models.CharField(max_length=255)
    keywords = models.TextField()

    def __str__(self):
        return self.title