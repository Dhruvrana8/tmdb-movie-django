from django.urls import path, include
from .views import TMDB_Movies_View

urlpatterns = [
    path('movies/', TMDB_Movies_View.as_view(), name='todo'),
]
