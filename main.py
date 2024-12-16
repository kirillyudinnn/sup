# main.py
from kinopoisk_api import KinopoiskClient, ForbiddenError, UnauthorizedError
import os

def main():
    API_KEY = os.environ.get('KINOPOISK_API_KEY', '9ZBJMNG-FHF4VDY-HXQ8EGE-4HH89SW')

    client = KinopoiskClient(API_KEY)

    try:
        movie_response = client.search_movie("Интерстеллар", page=1, limit=1)
        if movie_response.docs:
            movie = movie_response.docs[0]
            print(f"Movie ID: {movie.id}")
            print(f"Name: {movie.name}")
            print(f"Alternative Name: {movie.alternativeName}")
            print(f"Year: {movie.year}")
            print(f"Description: {movie.description}")
            print(f"Rating (KP): {movie.rating.kp if movie.rating else 'N/A'}")
            print(f"Genres: {', '.join([genre.name for genre in movie.genres]) if movie.genres else 'N/A'}")

            person_response = client.get_persons_by_movie(movie_id=movie.id, limit=5)
            print("\nActors:")
            for person in person_response.docs:
                print(f"{person.name} ({person.enName}), Age: {person.age}, Sex: {person.sex}")
        else:
            print("Movie not found.")
    except UnauthorizedError as e:
        print(f"Unauthorized Error: {e}")
    except ForbiddenError as e:
        print(f"Forbidden Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
