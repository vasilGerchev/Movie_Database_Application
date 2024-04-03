import json
import sys
import requests

OMDB_API_KEY = "75e112ac"


def add_movie(title, desc, date, director, genre):
    """Add a new movie to the database."""
    movie_id = generate_movie_id()
    rating = get_movie_rating(title)
    new_movie = {
        "id": movie_id,
        "title": title,
        "year": int(date),
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
        with open("movies_database.json", "r") as f:
            movies = json.load(f)
    except FileNotFoundError:
        movies = []
    return movies


def save_movies_to_database(movies):
    """Save movies to the JSON database."""
    with open("movies_database.json", "w") as f:
        json.dump(movies, f, indent=4)


def get_movie_rating(title):
    """Fetch movie Rating from the OMDb API."""
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            movie_data = data['imdbRating']
            return movie_data
    return None


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python movadd.py <title> <desc> <date> <director> <genre>")
        sys.exit(1)

    title, desc, date, director, genre = sys.argv[1:]
    add_movie(title, desc, date, director, genre)
