import json
from collections import Counter
import login

# Load the JSON file from movie database
with open('movies_database.json') as f:
    movie_data = json.load(f)

# Load the JSON file from favorites database
with open('favorite_movies.json') as f:
    favorite_movie_database = json.load(f)


# Define a function to sort movies by genre
def sort_movies_by_genre(movie_data):
    sorted_movies = {}
    for movie in movie_data:
        genre = movie['genre']
        if genre not in sorted_movies:
            sorted_movies[genre] = []
        sorted_movies[genre].append(movie)
    return sorted_movies


# Define a function to sort movies by newest
def sort_movies_by_newest(favorite_movie_database):
    return sorted(movie_data, key=lambda x: x['year'], reverse=True)


# Define a function to sort movies by liked
def top_5_liked_movies(favorite_movie_database):
    # Count occurrences of each movie id
    id_counts = Counter(movie['id'] for movie in favorite_movie_database)

    # Get top 5 most common movie ids
    top_5_ids = [id for id, count in id_counts.most_common(5)]

    # Get movie details for the top 5 ids
    top_5_movies = [{'id': movie_id, 'count': count} for movie_id, count in id_counts.items() if movie_id in top_5_ids]

    return top_5_movies


# Call the function to sort movies by genre
sorted_movies_by_genre = sort_movies_by_genre(movie_data)

# Print the sorted movies by genre
print("\nSortest by Genre:")
for genre, movies in sorted_movies_by_genre.items():
    print(f"Genre: {genre}")
    for movie in movies[:5]:
        print(f"\t{movie['title']}")

# Call the function to sort movies by newest
sorted_movies_by_newest = sort_movies_by_newest(movie_data)

# Print the sorted movies by newest
print("\nSorted by Newest:")
for movie in sorted_movies_by_newest[:5]:
    print(f"\t{movie['title']} ({movie['year']})")

# Call the function to sort movies by liked
top_5_liked_movies(favorite_movie_database)

# Print the sorted movies by most liked
print("\nSorted by Most Liked:")
sorted_top_5_movies = sorted(top_5_liked_movies(favorite_movie_database), key=lambda x: x['count'], reverse=True)
for movie in sorted_top_5_movies[:5]:  # Print only the top 5 most liked movies
    movie_details = next((item for item in movie_data if item["id"] == movie["id"]), None)
    if movie_details:
        print(f"\t{movie_details['title']} (Likes: {movie['count']})")