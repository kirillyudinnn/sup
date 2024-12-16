# client.py
import requests
from typing import Optional
from .models import MovieSearchResponse, PersonSearchResponse
from .exceptions import UnauthorizedError, ForbiddenError

class KinopoiskClient:
    BASE_URL = 'https://api.kinopoisk.dev'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def _get(self, endpoint: str, params: dict = None):
        headers = {'X-API-KEY': self.api_key}
        response = requests.get(f'{self.BASE_URL}{endpoint}', headers=headers, params=params)
        if response.status_code == 401:
            raise UnauthorizedError('Invalid API key or missing authorization.')
        elif response.status_code == 403:
            raise ForbiddenError('Daily request limit exceeded.')
        response.raise_for_status()
        return response.json()

    def search_movie(self, query: str, page: int = 1, limit: int = 10) -> MovieSearchResponse:
        endpoint = '/v1.4/movie/search'
        params = {
            'query': query,
            'page': page,
            'limit': limit
        }
        data = self._get(endpoint, params=params)
        return MovieSearchResponse(**data)

    def get_persons_by_movie(self, movie_id: int, page: int = 1, limit: int = 100, age_min: int=18, age_max: int=100) -> PersonSearchResponse:
        endpoint = '/v1.4/person'
        params = {
            'page': page,
            'limit': limit,
            'movies.id': movie_id,
            'movies.enProfession': 'actor',
            'age': f'{age_min}-{age_max}'
        }
        data = self._get(endpoint, params=params)
        return PersonSearchResponse(**data)
