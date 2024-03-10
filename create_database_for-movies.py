import json
from pathlib import Path


def create_movie_database():
    # Define the path to the JSON file
    db_path = Path("movies.json")

    # Initialize an empty database if the file doesn't exist
    if not db_path.exists():
        with open(db_path, "w") as f:
            json.dump([], f)


def load_movies_from_database():
    # Load movies from the JSON database
    with open("movies.json", "r") as f:
        movies = json.load(f)
    return movies


def save_movies_to_database(movies):
    # Save movies to the JSON database
    with open("movies.json", "w") as f:
        json.dump(movies, f, indent=4)


# Create the movie database
create_movie_database()
