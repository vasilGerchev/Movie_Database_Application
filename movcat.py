import json
import user
import json



# Load the JSON file
with open('favorite_movies.json') as f:
    movie_data = json.load(f)


# Define a function to sort movies by genre
def sort_movies_by_genre(movie_data):
    sorted_movies = {}
    for movie in movie_data:
        genre = movie['genre']
        if genre not in sorted_movies:
            sorted_movies[genre] = []
        sorted_movies[genre].append(movie)
    return sorted_movies


# Call the function to sort movies by genre
sorted_movies_by_genre = sort_movies_by_genre(movie_data)

# Print the sorted movies by genre
for genre, movies in sorted_movies_by_genre.items():
    print(f"Genre: {genre}")
    for movie in movies:
        print(f"\t{movie['title']}")

