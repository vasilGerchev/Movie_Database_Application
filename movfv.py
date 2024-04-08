import json
import sqlite3
import sys
import movdt
import login


def create_favorite_database():
    # Connect to SQLite database
    connection = sqlite3.connect('movie_database.db')
    c = connection.cursor()

    # Create 'favorites' table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXIST favorites title TEXT id TEXT user_id TEXT''')

    # Commit changes and close connection
    connection.commit()
    connection.close()


def search_movie_by_id(movie_id):
    """Search for movie ID in database"""
    movies = movdt.load_movies_from_database(movie_id)
    found_movies = []
    for movie in movies:
        if movie['id'] == movie_id:
            found_movies.append(movie)
    if found_movies:
        for found_movie in found_movies:
            print("The movie:", found_movie["title"], "Was added to favorites")
        return found_movies
    else:
        print("The movie does not exist")
        return None


def load_movie_from_favorite_movie():
    # Load movie from favorites table
    connection = sqlite3.connect('movie_database.db')
    c = connection.cursor()
    c.execute("SELECT * FROM favorites")
    movies = c.fetchall()
    connection.close()
    return movies


def check_for_exist_in_favorite(movie_title, user_id, favorities):
    """Check if a movie with the same title exists for a different user ID."""
    for movie in favorities:
        if movie[2] == movie_title and movie[3] == user_id:
            return True
    return False


def save_movie_to_favorite_movie(new_movies):
    # Save movies to the JSON database.
    existing_movies = load_movie_from_favorite_movie()
    connection = sqlite3.connect('movie_database.db')
    c = connection.cursor()
    for movie in new_movies:
        if check_for_exist_in_favorite(movie['title'], login.username, existing_movies):
            print(f"The movie with ID: {movie['id']} is already exist in favorites")
            return
        c.execute("INSERT INTO favorites (title, id, user_id) VALUES (?, ?, ?)",
                  (movie['title'], movie['id'], login.username))
    connection.commit()
    connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python movfv.py <movie_id>")
        sys.exit(1)

    try:
        movie_id = str(sys.argv[1])
    except ValueError:
        print("Error: <movie_id> must be an integer.")
        sys.exit(1)

    found_movies = search_movie_by_id(movie_id)
    if found_movies:
        create_favorite_database()
        save_movie_to_favorite_movie(found_movies)
