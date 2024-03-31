import json
import login

def movlst():
    """List all movies from the JSON file."""
    movies = load_movies_from_database()
    for movie in movies:
        print("Title:", movie["title"])
        print("Description", movie["description"])
        print("Year:", movie["year"])
        print("Director:", movie["director"])
        print("Genre:", movie["genre"])
        print("Rating", movie["rating"])
        print()


def load_movies_from_database():
    """Load movies from the JSON database."""
    with open("movies_database.json", "r") as f:
        movies = json.load(f)
    return movies


if __name__ == "__main__":
    movlst()
