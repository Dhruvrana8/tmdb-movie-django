import csv
from django.core.management.base import BaseCommand
from TMDB_api.models import TMDB_Movies  # Make sure this matches your actual model
from django.utils.dateparse import parse_date

class Command(BaseCommand):
    help = 'Import movies from a CSV file'

    def handle(self, *args, **kwargs):
        # Path to your CSV file
        csv_file_path = '/Users/dhruv/code/Machine Learning/Projects/TMDB/movieRecEngineDjango/TMDB/data/clear_TMDB_movie_dataset_v11.csv'
        
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Loop over the rows in the CSV and add them to the database
            for row in reader:
                # Handle each row in the CSV
                movie_data = {
                    'id': row['id'],
                    'title': row['title'],
                    'vote_average': row['vote_average'],
                    'vote_count': row['vote_count'],
                    'status': row['status'],
                    'release_date': parse_date(row['release_date']),
                    'revenue': row['revenue'],
                    'runtime': row['runtime'],
                    'adult': row['adult'] == 'True',  # Converting 'True'/'False' to boolean
                    'backdrop_path': row['backdrop_path'],
                    'budget': row['budget'],
                    'homepage': row['homepage'],
                    'imdb_id': row['imdb_id'],
                    'original_language': row['original_language'],
                    'original_title': row['original_title'],
                    'overview': row['overview'],
                    'popularity': row['popularity'],
                    'poster_path': row['poster_path'],
                    'tagline': row['tagline'],
                    'genres': row['genres'],
                    'production_companies': row['production_companies'],
                    'production_countries': row['production_countries'],
                    'spoken_languages': row['spoken_languages'],
                    'keywords': row['keywords'],
                }

                # Create the movie record in the database
                TMDB_Movies.objects.update_or_create(
                    id=movie_data['id'],  # This will update an existing movie if it exists
                    defaults=movie_data
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported movies data.'))
