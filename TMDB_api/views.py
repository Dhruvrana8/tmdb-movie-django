from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Q

from .models import TMDB_Movies
from .serializer import TMDB_Movie_Serializer
from .pagination import CustomPageNumberPagination

# Create your views here.


class TMDB_Movies_View(APIView):
    def get(self, request, id=None):
        movies = TMDB_Movies.objects.all()

        # Handle search query
        search_query = request.query_params.get('search', None)
        if search_query:
            movies = movies.filter(
                Q(title__icontains=search_query.strip()) |
                Q(original_title__icontains=search_query.strip())
            )

        paginator = CustomPageNumberPagination()
        paginated_todos = paginator.paginate_queryset(movies, request)
        serialized_data = TMDB_Movie_Serializer(paginated_todos, many=True)
        return paginator.get_paginated_response(serialized_data.data)
