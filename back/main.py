import dotenv
import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from bson import ObjectId
from pycine import moviemodels
from pycine import personModels
import motor.motor_asyncio
from pymongo import ReturnDocument
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pycine import tmdb

dotenv.load_dotenv(".env") 
uri = os.environ.get("MONGODB")
client = motor.motor_asyncio.AsyncIOMotorClient(uri)
db = client['tmdb'] 


app = FastAPI()

origins = [
 "http://localhost",
 "http://localhost:*",
 "http://localhost:5173",
]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)


@app.get("/")
def hello():
    return{"status":"pycine is running"}


@app.get("/movie/{id}")
def get_movie(id:int):
    return tmdb.get_movie(id)

@app.get("/movie")
def search_movies():
    params = {
        "sort_by": "vote_average.desc"
    }
    return tmdb.search_movies(params)


@app.get("/movies/top")
def search_movies():
    return tmdb.search_movies()

@app.get("/save/movie",
    response_description="List all movies",
    response_model=moviemodels.MovieCollection,
    response_model_by_alias=False,
)
async def list_movies():
    movies_collection = db.get_collection("movies")
    return moviemodels.MovieCollection(movies=await movies_collection.find().to_list(20))

@app.post("/save/movie",
    response_model=moviemodels.Movie,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def save_movie(movie: moviemodels.Movie = Body(...)):
    movies_collection = db.get_collection("movies")
    movie_id = str(movie.id)
    existing_movie = await movies_collection.find_one({"_id": movie_id})
    if existing_movie:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Filme já cadastrado."
        )
    movie.is_fav = True
    movie_data = movie.model_dump(by_alias=True)
    await movies_collection.insert_one(movie_data)
    created_movie = await movies_collection.find_one({"_id": movie_id})    
    return created_movie  



@app.delete("/remove/movie/{id}",
    response_description="Remove movie by id",
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def remove_movie(id: str):
    movies_collection = db.get_collection("movies")
    deleted_result = await movies_collection.delete_one({'_id': id})
    if deleted_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully"}



@app.get("/person/{id}")
def get_person(id:int):
    return tmdb.get_person(id)

@app.get("/person/{id}/allmovies")
def get_person(id:int):
    return tmdb.get_person_movies(id)

@app.get("/byname/person/{name}")
def search_person(name:str):
    return tmdb.search_person(name)

@app.get("/trending/person/{type}")
def treding_person(type:str):
    return tmdb.treding_person(type)


@app.get("/popular/person")
def treding_person():
    return tmdb.popular_person()


@app.get("/save/person", 
    response_description="List all Persons",
    response_model=personModels.PersonCollection,
    response_model_by_alias=False,
)
async def list_person():
    persons_collection = db.get_collection("persons")
    return personModels.PersonCollection(persons=await persons_collection.find().to_list(20))

@app.post("/save/person",
    response_model=personModels.Person,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def save_artist(person: personModels.Person = Body(...)):
    persons_collection = db.get_collection("persons")
    person_id = str(person.id)
    existing_artist = await persons_collection.find_one({"_id": person_id})
    if existing_artist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Artista já cadastrado."
        )
    person.is_fav = True
    person_data = person.model_dump(by_alias=True)
    await persons_collection.insert_one(person_data)
    created_person = await persons_collection.find_one({"_id": person_id})    
    return created_person 

@app.delete("/remove/person/{id}",
    response_description="Remove artist by id",
    status_code=status.HTTP_200_OK,
    response_model_by_alias=False,
)
async def remove_artist(id: str):
    persons_collection = db.get_collection("persons")
    deleted_result = await persons_collection.delete_one({'_id': id})
    if deleted_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"message": "Person deleted successfully"}



    