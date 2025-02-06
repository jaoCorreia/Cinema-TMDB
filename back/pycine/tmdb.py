
import os 
import dotenv
dotenv.load_dotenv(".env")
token = os.environ["API_TOKEN"]
import requests
from pycine.moviemodels import Movie
from pycine.moviemodels import MovieResults
from pycine.personModels import Person
from pycine.personModels import PersonResults


def get_json(url: str, params: dict = None) -> dict:
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    data = requests.get(url, headers=headers, params=params)
    return data.json()

def get_movie(id: int):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    data = get_json(url)
    movie = Movie.model_validate(data)
    return movie

def search_movies(params: dict = None):
    url = f"https://api.themoviedb.org/3/discover/movie"
    params or {
        "include_adult": False, 
        "include_video": False, 
        "language": "en_Us", 
        "page": 1, 
        "sort_by": "popularity.desc"
    }
    data = get_json(url,params) 
    return MovieResults.model_validate(data)

def get_person(id : int):
    url = f"https://api.themoviedb.org/3/person/{id}"
    data = get_json(url)
    return Person.model_validate(data) 

def get_person_movies(id):
    url = f"https://api.themoviedb.org/3/person/{id}/movie_credits"
    data = get_json(url)
    results = {
        "results" : data.get("cast"), 
        "page": 1, 
        "total_pages": 1, 
        "total_results": len(data.get("cast"))
    }
    return MovieResults.model_validate(results)
     

def search_person(name: str,params: dict = None):
    url = f"https://api.themoviedb.org/3/search/person?query={name}"
    data = get_json(url,params)
    return PersonResults.model_validate(data) 

def treding_person(type : str, params: dict = None):
    url = f"https://api.themoviedb.org/3/trending/person/{type}"
    data = get_json(url)
    return PersonResults.model_validate(data)
        
def popular_person(params: dict = None):
    url = f'https://api.themoviedb.org/3/person/popular'
    params or {
        "page": 1, 
    }
    data = get_json(url,params)
    return PersonResults.model_validate(data)

