from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class Favorite(BaseModel):
    type: str # 'movie' || 'character'
    name: str
    url: str
    
    class Config:
        schema_extra = {
            "example": {
                "type": "movie",
                "name": "A New Hope",
                "url" : "https://swapi.dev/api/films/1/"
            }
        }
class updateFavoriteModel(BaseModel):
    type: Optional[str]
    name: Optional[str]
    url: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "type": "movie",
                "name": "A New Hope",
                "url": "https://swapi.dev/api/films/1/"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }