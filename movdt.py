import json
import sys
import login


def get_movie_details(movie_id):
    """Get details of a movie by its ID."""
    movies = load_movies_from_database()
    for movie in movies:
        if movie['id'] == movie_id:
            print_movie_details(movie)
            return
    print("Movie not found.")


def load_movies_from_database():
    """Load movies from the JSON database."""
    with open("movies_database.json", "r") as f:
        movies = json.load(f)
    return movies


def print_movie_details(movie):
    """Print details of a movie."""
    print("Title:", movie["title"])
    print("Description", movie["description"])
    print("Year:", movie["year"])
    print("Director:", movie["director"])
    print("Genre:", movie["genre"])
    print("User Ratings:", movie["rating"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python movdt.py <movie_id>")
        sys.exit(1)

    try:
        movie_id = int(sys.argv[1])
    except ValueError:
        print("Error: <movie_id> must be an integer.")
        sys.exit(1)

    get_movie_details(movie_id)
