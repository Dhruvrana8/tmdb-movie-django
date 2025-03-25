from rest_framework import serializers
from .models import TMDB_Movies

class TMDB_Movie_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TMDB_Movies
        fields = '__all__'  # This will include all fields from the Movie model
