import sqlite3
from collections import Counter

# Connect to the SQLite database
conn = sqlite3.connect('movie_database.db')
cursor = conn.cursor()


# Define a function to load movie data from the database
def load_movie_data():
    cursor.execute("SELECT * FROM movies")
    return cursor.fetchall()


# Define a function to load favorite movie data from the database
def load_favorite_movie_data():
    cursor.execute("SELECT * FROM favorites")
    return cursor.fetchall()


# Define a function to sort movies by genre
def sort_movies_by_genre(movie_data):
    sorted_movies = {}
    for movie in movie_data:
        genre = movie[2]  # Assuming 'genre' is at index 2 in the database table
        if genre not in sorted_movies:
            sorted_movies[genre] = []
        sorted_movies[genre].append(
            {'id': movie[0], 'title': movie[1]})  # Assuming 'id' is at index 0 and 'title' is at index 1
    return sorted_movies


# Define a function to sort movies by newest
def sort_movies_by_newest(movie_data):
    return sorted(movie_data, key=lambda x: x[3], reverse=True)  # Assuming 'year' is at index 3


# Define a function to sort movies by liked
def top_5_liked_movies(favorite_movie_data):
    id_counts = Counter(movie[1] for movie in favorite_movie_data)  # Assuming 'movie_id' is at index 1

    # Get top 5 most common movie ids
    top_5_ids = [id for id, count in id_counts.most_common(5)]

    # Get movie details for the top 5 ids
    top_5_movies = [{'id': movie_id, 'count': count} for movie_id, count in id_counts.items() if movie_id in top_5_ids]

    return top_5_movies


# Fetch movie data from the database
movie_data = load_movie_data()

# Fetch favorite movie data from the database
favorite_movie_data = load_favorite_movie_data()

# Call the function to sort movies by genre
sorted_movies_by_genre = sort_movies_by_genre(movie_data)

# Print the sorted movies by genre
print("\nSorted by Genre:")
for genre, movies in sorted_movies_by_genre.items():
    print(f"Genre: {genre}")
    for movie in movies[:5]:
        print(f"\t{movie['title']}")

# Call the function to sort movies by newest
sorted_movies_by_newest = sort_movies_by_newest(movie_data)

# Print the sorted movies by newest
print("\nSorted by Newest:")
for movie in sorted_movies_by_newest[:5]:
    print(f"\t{movie[1]} ({movie[3]})")  # Assuming 'title' is at index 1 and 'year' is at index 3

# Call the function to sort movies by liked
top_5_liked_movies(favorite_movie_data)

# Print the sorted movies by most liked
print("\nSorted by Most Liked:")
sorted_top_5_movies = sorted(top_5_liked_movies(favorite_movie_data), key=lambda x: x['count'], reverse=True)
for movie in sorted_top_5_movies[:5]:  # Print only the top 5 most liked movies
    cursor.execute("SELECT title FROM movies WHERE id = ?", (movie["id"],))  # Fetch movie title from movies table
    movie_title = cursor.fetchone()
    if movie_title:
        print(f"\t{movie_title[0]} (Likes: {movie['count']})")

# Close the database connection
conn.close()
