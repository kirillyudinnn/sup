from typing import Optional, List
from pydantic import BaseModel

class Name(BaseModel):
    name: Optional[str] = None
    language: Optional[str] = None
    type: Optional[str] = None

class ExternalId(BaseModel):
    kpHD: Optional[str] = None
    imdb: Optional[str] = None
    tmdb: Optional[int] = None

class Logo(BaseModel):
    url: Optional[str] = None

class Poster(BaseModel):
    url: Optional[str] = None
    previewUrl: Optional[str] = None

class Backdrop(BaseModel):
    url: Optional[str] = None
    previewUrl: Optional[str] = None

class Rating(BaseModel):
    kp: Optional[float] = None
    imdb: Optional[float] = None
    tmdb: Optional[float] = None
    filmCritics: Optional[float] = None
    russianFilmCritics: Optional[float] = None

class Votes(BaseModel):
    kp: Optional[int] = None
    imdb: Optional[int] = None
    tmdb: Optional[int] = None
    filmCritics: Optional[int] = None
    russianFilmCritics: Optional[int] = None

class Genre(BaseModel):
    name: Optional[str] = None

class Country(BaseModel):
    name: Optional[str] = None

class ReleaseYear(BaseModel):
    start: Optional[int] = None
    end: Optional[int] = None

class Movie(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    alternativeName: Optional[str] = None
    enName: Optional[str] = None
    type: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None
    shortDescription: Optional[str] = None
    movieLength: Optional[int] = None
    names: Optional[List[Name]] = None
    externalId: Optional[ExternalId] = None
    logo: Optional[Logo] = None
    poster: Optional[Poster] = None
    backdrop: Optional[Backdrop] = None
    rating: Optional[Rating] = None
    votes: Optional[Votes] = None
    genres: Optional[List[Genre]] = None
    countries: Optional[List[Country]] = None
    releaseYears: Optional[List[ReleaseYear]] = None
    isSeries: Optional[bool] = None
    ticketsOnSale: Optional[bool] = None
    totalSeriesLength: Optional[int] = None
    seriesLength: Optional[int] = None
    ratingMpaa: Optional[str] = None
    ageRating: Optional[int] = None
    top10: Optional[int] = None
    top250: Optional[int] = None
    typeNumber: Optional[int] = None
    status: Optional[str] = None

class MovieSearchResponse(BaseModel):
    docs: Optional[List[Movie]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None

class Person(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    enName: Optional[str] = None
    photo: Optional[str] = None
    sex: Optional[str] = None
    age: Optional[int] = None

class PersonSearchResponse(BaseModel):
    docs: Optional[List[Person]] = None
    total: Optional[int] = None
    limit: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None
