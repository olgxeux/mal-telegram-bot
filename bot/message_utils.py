from bot.keyboards.inline_keybords import get_users_media_kb, get_search_media_kb
from database.gql_manager import *
from utils import type_to_list_name


async def media_message_params(media_type: str, user: dict, media_id: int, from_page: int, search_prompt: str | None = None):
    list_name = type_to_list_name(media_type)

    users_media = None
    for m in user[list_name]:
        if int(m["Id"]) == media_id:
            users_media = m
            break
    is_in_users_list = False
    if users_media:
        is_in_users_list = True

    gql_media = (await get_media(media_id))["Media"]
    image = gql_media["coverImage"]["extraLarge"]

    text_parts = []
    text_parts.append(
        f"{gql_media['title']['userPreferred']} ({gql_media['format']})\n\n")
    if is_in_users_list:
        text_parts.append(f"Your rating: {users_media['Rating']} ⭐️\n")
        text_parts.append(f"Your status: {users_media['Status']}\n\n")
    text_parts.append(f"Info:\nYear: {gql_media['startDate']['year']}\n")
    text_parts.append(
        f"Rating on AniList: {gql_media['averageScore'] / 10} ⭐️\n")
    text_parts.append(f"Status: {gql_media['status']}")

    message_text = "".join(text_parts)

    if is_in_users_list:
        kb = await get_users_media_kb(media_type, gql_media, from_page)
    else:
        kb = await get_search_media_kb(media_type, gql_media, from_page, search_prompt)

    return image, message_text, kb
