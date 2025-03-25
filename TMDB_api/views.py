from django.shortcuts import render
from rest_framework.views import APIView

from .models import TMDB_Movies
from .serializer import TMDB_Movie_Serializer
from .pagination import CustomPageNumberPagination

# Create your views here.
class TMDB_Movies_View(APIView):
    def get(self, request, id=None):
        movies = TMDB_Movies.objects.all()
        
        paginator = CustomPageNumberPagination()
        paginated_todos = paginator.paginate_queryset(movies, request)
        serialized_data = TMDB_Movie_Serializer(paginated_todos, many=True)
        return paginator.get_paginated_response(serialized_data.data)