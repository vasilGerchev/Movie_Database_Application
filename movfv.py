import json
import sys
import movdt
import login

print(login.user)


def create_favorite_database():
    # Define the path to the JSON file
    db_path = Path("favorite_database.json")

    # Initialize an empty database if the file doesn't exist
    if not db_path.exists():
        with open(db_path, "w") as f:
            json.dump([], f)


def search_movie_by_id(movie_id):
    """Search for movie ID in database"""
    movies = movdt.load_movies_from_database()
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
    """Load movies from the JSON database."""
    try:
        with open("favorite_movies.json", "r") as f:
            movies = json.load(f)
    except FileNotFoundError:
        movies = []
    return movies


def check_for_exist_in_favorite(movie_title, user_id, favorities):
    """Check if a movie with the same title exists for a different user ID."""
    for movie in favorities:
        if movie.get('title') == movie_title and movie.get('user id') == user_id:
            return True
    return False


def save_movie_to_favorite_movie(new_movies):
    """Save movies to the JSON database."""
    existing_movies = load_movie_from_favorite_movie()  # Load existing favorite movies
    if existing_movies is None:  # If file not found or empty, initialize as empty list
        existing_movies = []
    for movie in new_movies:
        if check_for_exist_in_favorite(movie['title'], login.user, existing_movies):
            print(f"The movie with ID: {movie['id']} is already exist in favorite")
            return
    simplified_movie = {'id': movie['id'], 'title': movie['title'], 'user id': login.user}
    existing_movies.append(simplified_movie)  # Append new movies to existing list

    with open("favorite_movies.json", "w") as f:
        json.dump(existing_movies, f, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python movfv.py <movie_id>")
        sys.exit(1)

    try:
        movie_id = int(sys.argv[1])
    except ValueError:
        print("Error: <movie_id> must be an integer.")
        sys.exit(1)

    found_movies = search_movie_by_id(movie_id)
    save_movie_to_favorite_movie(found_movies)
