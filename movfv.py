import sys
from pathlib import Path
import sqlite3
from login import client, login
import movdt


def create_favorite_database():
    # Connect to SQLite database
    conn = sqlite3.connect("movie_database.db")
    c = conn.cursor()

    # Create 'favorites' table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS favorites
                 (id TEXT, title TEXT, user_id TEXT)''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


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
            "title": movie[1]
        }
    else:
        return None


def load_movie_from_favorite_movie():
    """Load movies from the favorites table."""
    conn = sqlite3.connect("movie_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM favorites")
    movies = c.fetchall()
    conn.close()
    return movies


def check_for_exist_in_favorite(movie_title, user_id, favorites):
    """Check if a movie with the same title exists for a different user ID."""
    for movie in favorites:
        if movie[1] == movie_title and movie[0] == user_id:
            return True
    return False


def save_movie_to_favorite_movie(new_movies):
    """Save movies to the favorites table."""
    existing_movies = load_movie_from_favorite_movie()
    conn = sqlite3.connect("movie_database.db")
    c = conn.cursor()
    for movie in new_movies:
        if check_for_exist_in_favorite(movie['title'], login.username, existing_movies):
            print(f"The movie with ID: {movie['id']} is already exist in favorites")
            return
        c.execute("INSERT INTO favorites (id, title, user_id) VALUES (?, ?, ?)",
                  (movie['id'], movie['title'], login.username))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python movfv.py <movie_id>")
        sys.exit(1)

    try:
        movie_id = str(sys.argv[1])
    except ValueError:
        print("Error: <movie_id> must be an text.")
        sys.exit(1)

    found_movies = load_movies_from_database(movie_id)
    if found_movies:
        create_favorite_database()
        save_movie_to_favorite_movie(found_movies)
