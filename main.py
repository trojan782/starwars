from typing import Optional
from utils.config import get_settings, Settings
from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException 
from models.index import Favorite
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        url = 'https://swapi.dev/api/people/'
        res = requests.get(url)
        return res.json()
    except HTTPException:
        return {'message': 'Something went please wrong, try again'}


@app.get('/favorites')
async def get_fav():
    return{'message': 'Feature coming soon!'}

