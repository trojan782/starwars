from urllib import response
from utils.config import get_settings, Settings
# from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models import index
from fastapi.middleware.cors import CORSMiddleware
from db import database
import requests
from models.index import Favorite, ResponseModel
from repository import FavoriteRepo
app = FastAPI()
#create the database tables on app startup or reload

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ping endpoint
@app.get('/ping')
async def ping(settings: Settings = Depends(get_settings)):
    return {
        "Staus": "Server is live!",
        "environment": settings.environment, 
        "testing": settings.testing
    }
@app.get('/', response_description="Home")
async def welcome():
    return {"message": "Welcome to our starwars favorite, kindly explore all your starwars related things!", 
            "link": "http://127.0.0.1:8000/docs"}

# endpoint to return all people
@app.get('/people', response_description="Return all people")
async def get_people():
    try:
       url = 'https://swapi.dev/api/people'
       res = requests.get(url)
       return res.json()
    except HTTPException:
       return {'message': 'Something went please wrong, try again'}


# To retrive a single person
@app.get("/people/{id}", response_description="Get a single person")
async def get_person(id):
    try:
        url = f'https://swapi.dev/api/people/{id}'
        person = requests.get(url)
        if person is not None:
            return person.json()
    except:
        raise HTTPException(status_code=404, detail=f"Person {id} not found")
        
        
# endpoint to return all movies from swapi
@app.get('/films', response_description="Return all movies")
async def get_movies():
    try:
        url = 'https://swapi.dev/api/films'
        res = requests.get(url)
        return res.json()
    except HTTPException:
        return {'message': 'Something went please wrong, try again'}


#Endpoint to get all favorites
@app.get("/favorites", response_description= "Retrive all favorites")
async def get_favorites():
    favs = await FavoriteRepo.retrive_favorites()
    if favs:
        return ResponseModel(favs, "Favorites retrived successfully")
    return ResponseModel(favs, "empty list")

@app.get('/favorites/{id}', response_description="Return a saved favorite with its id")
async def get_favorite(id):
    fav = await FavoriteRepo.retrive_favorite(id)
    if fav:
        return ResponseModel(fav, "Favorite Successfully retrived!")
    return ResponseModel(fav, "Empty List!")

# Endpoint to create a new favorite
@app.post("/favorite", response_description="create a new fav")
async def create_fav(fav: Favorite = Body(...)):
    fav = jsonable_encoder(fav)
    new_fav = await FavoriteRepo.create_fav(fav)
    return ResponseModel(new_fav, "Fav added successfully.")


