import json
import sys


def add_movie(title, desc, date, director, genre, rating):
    """Add a new movie to the database."""

    movie_id = generate_movie_id()
    new_movie = {
        "id": movie_id,
        "title": title,
        "year": date,
        "director": director,
        "genre": genre,
        "description": desc,
        "rating": rating
    }
    movies = load_movies_from_database()
    movies.append(new_movie)
    save_movies_to_database(movies)
    print("New movie added successfully.")


def generate_movie_id():
    """Generate a new unique ID for the movie."""
    movies = load_movies_from_database()
    if not movies:
        return 1
    return max(movie['id'] for movie in movies) + 1


def load_movies_from_database():
    """Load movies from the JSON database."""
    try:
        with open("movies.json", "r") as f:
            movies = json.load(f)
    except FileNotFoundError:
        movies = []
    return movies


def save_movies_to_database(movies):
    """Save movies to the JSON database."""
    with open("movies.json", "w") as f:
        json.dump(movies, f, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python movadd.py <title> <desc> <date> <director> <genre> <rating>")
        sys.exit(1)

    title, desc, date, director, genre, rating = sys.argv[1:]
    add_movie(title, desc, date, director, genre, rating)
