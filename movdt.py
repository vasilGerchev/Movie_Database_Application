import sqlite3
import sys


def get_movie_details(movie_id):
    """Get details of a movie by its ID."""
    movie = load_movies_from_database(movie_id)
    if movie:
        print_movie_details(movie)
    else:
        print("Movie not found.")


def load_movies_from_database(movie_id):
    """Load a movie from the SQLite database."""

    connection = sqlite3.connect('movie_database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies WHERE id=?", (movie_id,))
    movie = cursor.fetchone()
    connection.close()

    if movie:
        return {
            "id": movie[0],
            "title": movie[1],
            "year": movie[2],
            "director": movie[3],
            "genre": movie[4],
            "description": movie[5],
            "rating": movie[6]
        }
    else:
        return None


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
        movie_id = str(sys.argv[1])
    except ValueError:
        print("Error: <movie_id> must be an string.")
        sys.exit(1)

    get_movie_details(movie_id)
