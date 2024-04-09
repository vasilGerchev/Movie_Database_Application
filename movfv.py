import sqlite3
import sys
import login


def check_and_save_favorite(movie_id):
    """Check if movie exists in movies table and save it to favorites."""
    connection = sqlite3.connect('movie_database.db')
    cursor = connection.cursor()

    # Check if the movie exists in the movies table
    cursor.execute('''SELECT id, title FROM movies WHERE id = ?''', (movie_id,))
    movie = cursor.fetchone()

    if movie:
        # Get logged user ID
        user_id = login.get_logged_user()

        # Check if the movie already exists in favorites for this user
        cursor.execute('''SELECT title FROM favorites WHERE user_id = ? AND title = ?''', (user_id, movie[1]))
        existing_movie = cursor.fetchone()

        if existing_movie:
            print("Error: The movie already exists in favorites for this user.")
        else:
            # Save the movie to the favorites table
            cursor.execute('''INSERT INTO favorites (user_id, id, title) VALUES (?, ?, ?)''',
                           (user_id, movie[0], movie[1]))
            connection.commit()
            print("Movie added to favorites successfully.")
    else:
        print("Error: Movie with given ID does not exist.")

    connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_and_save_favorite.py <movie_id>")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_and_save_favorite.py <movie_id>")
        sys.exit(1)

    movie_id = sys.argv[1]
    check_and_save_favorite(movie_id)
