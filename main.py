from utils.config import get_settings, Settings
from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException 
from models.index import Favorite
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

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
    
# endpoint to return all people
@app.get('/people')
async def get_people():
    try:
       url = 'https://swapi.dev/api/people'
       res = requests.get(url)
       return res.json()
    except HTTPException:
       return {'message': 'Something went please wrong, try again'}

# endpoint to return all movies
@app.get('/films')
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



# mongodb+srv://trojan1:<password>@cluster0.uaj88.mongodb.net/myFirstDatabase?retryWrites=true&w=majority