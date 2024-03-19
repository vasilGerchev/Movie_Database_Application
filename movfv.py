import json
import sys
import movdt


def search_movie_by_id(movie_id):
    movies = movdt.load_movies_from_database()
    found_movies = []
    for movie in movies:
        if movie['id'] == movie_id:
            found_movies.append(movie)
    if found_movies:
        for found_movie in found_movies:
            print("The movie:", movie["title"], "Was added to favorites")
        return found_movies
    else:
        print("The movie does not exist")
        return None


def save_movie_to_favorite_movie(movies):
    with open("favorite_movies.json", 'w') as file:
        json.dump(movies, file, indent=4)


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
