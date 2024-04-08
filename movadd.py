import sqlite3
import sys
import requests
import uuid
import login

OMDB_API_KEY = "75e112ac"


def add_movie(title, desc, date, director, genre):
    """Add a new movie to the database."""
    movie_id = generate_movie_id()
    rating = get_movie_rating(title)
    new_movie = {
        "id": str(movie_id),
        "title": title,
        "year": int(date),
        "director": director,
        "genre": genre,
        "description": desc,
        "rating": rating
    }
    save_movies_to_database(new_movie)
    print("New movie added successfully.")


def generate_movie_id():
    """Generate a new unique ID for the movie."""
    return str(uuid.uuid4())


def save_movies_to_database(movies):
    """Save movie to the SQLite database."""
    connection = sqlite3.connect('movie_database.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                            id TEXT PRIMARY KEY,
                            title TEXT,
                            year INTEGER,
                            director TEXT,
                            genre TEXT,
                            description TEXT,
                            rating REAL
                       )''')
    cursor.execute('''INSERT INTO movies (id, title, year, director, genre, description, rating) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (movies['id'], movies['title'], movies['year'], movies['director'], movies['genre'], movies['description'], movies['rating']))
    connection.commit()
    connection.close()


def get_movie_rating(title):
    """Fetch movie data from the OMDb API."""
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
