import json
import sys
import movdt
import user


def search_movies(query):
    '''Search for movies based on their titles.'''
    movies = movdt
    found_movies = []
    for movie in (movdt.load_movies_from_database()):
        if query.lower() in movie['title'].lower():
            found_movies.append(movie)
    if found_movies:
        print("Search results:")
        for found_movie in found_movies:
            (movdt.print_movie_details(found_movie))
    else:
        print("No movies found matching the search query.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python movsrch.py <enter the movie title>")
        sys.exit(1)

    search_query = sys.argv[1]
    search_movies(search_query)
