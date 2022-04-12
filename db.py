"""DATABASE
MongoDB database initialization
"""
import motor.motor_asyncio

MONGODB_URL = 'mongodb://127.0.0.1:27017/'

client =  motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# connect to database python_db
database = client.favorites

favorite_collection = database.get_collection("favorites")
print(favorite_collection)

def fav_helper(fav) -> dict:
    return {
        "id": str(fav["_id"]),
        "type": fav["type"],
        "name": fav["name"],
        "url": fav["url"],
    }