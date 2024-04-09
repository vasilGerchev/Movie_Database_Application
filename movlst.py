import sqlite3


def movlst():
    """List all movies from the database."""
    movies = load_movies_from_database()
    for movie in movies:
        print("Title:", movie["title"])
        print("Year:", movie["description"])
        print("Director:", movie["year"])
        print("Genre:", movie["director"])
        print("Description:", movie["genre"])
        print("Rating:", movie["rating"])
        print()


def load_movies_from_database():
    """Load movies from the SQLite database."""
    try:
        # Connect to the database
        conn = sqlite3.connect("movie_database.db")
        cursor = conn.cursor()

        # Fetch all movies from the database
        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall()

        # Convert fetched data to a list of dictionaries
        movies = []
        for row in rows:
            movie = {
                "title": row[1],
                "description": row[2],
                "year": row[3],
                "director": row[4],
                "genre": row[5],
                "rating": row[6]
            }
            movies.append(movie)

        return movies

    except sqlite3.Error as e:
        print("Error reading data from database:", e)

    finally:
        # Close the database connection
        if conn:
            conn.close()


if __name__ == "__main__":
    movlst()
