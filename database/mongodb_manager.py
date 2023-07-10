from loader import user_db
from utils import type_to_list_name
_user_collection = user_db["User"]


async def get_user(user_id: int) -> dict:
    user = await _user_collection.find_one({"id": user_id})
    return user


async def create_new_user(user_id: int) -> dict:
    new_user = {"id": user_id, "AnimeList": [], "MangaList": []}
    user = await _user_collection.insert_one(new_user)
    return await get_user(user.inserted_id)


async def add_media_for_user(media_type: str, user_id: int, new_media: dict) -> dict:
    list_name = type_to_list_name(media_type)
    user = await _user_collection.find_one_and_update(
        {"id": user_id}, {"$push": {list_name: new_media}}, return_document=True)
    return user


async def remove_media_from_user(media_type: str, user_id: int, media_id: int) -> dict:
    list_name = type_to_list_name(media_type)
    user = await _user_collection.find_one_and_update(
        {"id": user_id}, {"$pull": {list_name: {"Id": media_id}}}, return_document=True)
    return user


async def change_users_media_status(media_type: str, user_id: int, media_id: int, new_status: str) -> dict:
    list_name = type_to_list_name(media_type)
    user = await _user_collection.find_one_and_update(
        {"id": user_id, f"{list_name}.Id": media_id}, {"$set": {f"{list_name}.$.Status": new_status}}, return_document=True)
    return user


async def change_users_media_rating(media_type: str, user_id: int, media_id: int, new_rating: str) -> dict:
    list_name = type_to_list_name(media_type)
    user = await _user_collection.find_one_and_update(
        {"id": user_id, f"{list_name}.Id": media_id}, {"$set": {f"{list_name}.$.Rating": new_rating}}, return_document=True)
    return user
