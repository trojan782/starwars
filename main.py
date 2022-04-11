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
        
        
    
# endpoint to return all movies
@app.get('/films', response_description="Return all movies")
async def get_movies():
    try:
        url = 'https://swapi.dev/api/films'
        res = requests.get(url)
        return res.json()
    except HTTPException:
        return {'message': 'Something went please wrong, try again'}


# endpoint to return all your saved favorites 
@app.get('/favorites')
async def get_fav():
    return{'message': 'Feature coming soon!'}



# @app.get("/favorite", response_model=ResponseModel)
# async def get_all():
#     _favlist = await FavoriteRepo.get_fav()
#     print(_favlist)
#     return ResponseModel(code=200, status="Ok", message="Success retrieve all data", result=_favlist).dict(exclude_none=True)

@app.get("/home", response_description= "Retrive all favorites")
async def get_favorites():
    favs = await FavoriteRepo.retrive_favorites()
    if favs:
        return ResponseModel(favs, "Students retrived successfully")
    return ResponseModel(favs, "empty list")
        
# @app.post("/favorite", response_description="Get all favs", response_model=ResponseModel)
# async def create_fav(fav: Favorite = Body(...)):
#     fav = jsonable_encoder(fav)
#     new_fav = await database["favorites"].insert_one(fav)
#     created_fav = await database["favorites"].find_one({"_id": new_fav.inserted_id})
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_fav)


