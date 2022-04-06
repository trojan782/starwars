from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
class Favorite(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
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