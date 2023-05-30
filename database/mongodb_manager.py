import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from config import CONNECTION_STRING, DATABASE_NAME


client = AsyncIOMotorClient(CONNECTION_STRING)
db = client[DATABASE_NAME]
user_collection = db["User"]


async def get_user(user_id: int) -> dict:
    user = await user_collection.find_one({"id": user_id})
    return user


async def create_new_user(user_id: int) -> dict:
    new_user = {"id": user_id, "AnimeList": [], "MangaList": []}
    user = await user_collection.insert_one(new_user)
    return await get_user(user.inserted_id)


async def add_media_for_user(media_type: str, user_id: int, new_media: dict) -> dict:
    list_name = None
    if media_type == "anime":
        list_name = "AnimeList"
    elif media_type == "manga":
        list_name = "MangaList"

    user = await user_collection.find_one_and_update(
        {"id": user_id}, {"$push": {list_name: new_media}}, return_document=True)
    return user


async def delete_media_from_user(media_type: str, user_id: int, media_id: int) -> dict:
    list_name = None
    if media_type == "anime":
        list_name = "AnimeList"
    elif media_type == "manga":
        list_name = "MangaList"

    user = await user_collection.find_one_and_update(
        {"id": user_id}, {"$pull": {list_name: {"Id": media_id}}}, return_document=True)
    return user
