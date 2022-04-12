from typing import Collection
from models.index import Favorite

from db import database, favorite_collection, fav_helper

import uuid

class FavoriteRepo:
    @staticmethod
    async def retrive_favorites():
        _favorites = []
        async for fav in favorite_collection.find():
            _favorites.append(fav_helper(fav))
        return _favorites

    
    @staticmethod
    async def create_fav(fav_data: dict) -> dict:
        favorite = await favorite_collection.insert_one(fav_data)
        new_favorite = await favorite_collection.find_one({"_id": favorite.inserted_id})
        return fav_helper(new_favorite)
        
        
    @staticmethod
    async def retrive_favorite(id: str) -> dict:
        favorite = await favorite_collection.find_one({"_id": id})
        if favorite:
            return fav_helper(favorite)
        
        
    