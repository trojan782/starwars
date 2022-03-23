from pydantic import BaseModel
# from typing import Optional

class Favorite(BaseModel):
    type: str # 'movie' || 'character'
    name: str
    url: str
    
    
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }