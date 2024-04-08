import sqlite3
import sys


def search_movie_by_title(database_file, title):
    try:
        # Connect to the database
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        # Search for the movie by title
        cursor.execute("SELECT * FROM movies WHERE title LIKE ?", ('%' + title + '%',))
        rows = cursor.fetchall()

        # Display the fetched data
        if len(rows) == 0:
            print("No movies found with title:", title)
        else:
            for row in rows:
                print("Title:", row[1])
                print("Year:", row[2])
                print("Director:", row[3])
                print("Genre:", row[4])
                print("Description:", row[5])
                print("Rating:", row[6])
                print()

    except sqlite3.Error as e:
        print("Error reading data from database:", e)

    finally:
        # Close the database connection
        if connection:
            connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python movsrch.py <enter the movie title>")
        sys.exit(1)
    database_file = "movie_database.db"
    search_title = sys.argv[1]
    search_movie_by_title(database_file, search_title)
