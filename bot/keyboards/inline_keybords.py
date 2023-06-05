from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.mongodb_manager import get_user
from math import ceil
from utils import type_to_list_name


def get_main_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.row(InlineKeyboardButton(text="My anime",
           callback_data="view_list_anime_p_0"))  # type: ignore
    kb.row(InlineKeyboardButton(text="My manga",
           callback_data="view_list_manga_p_0"))  # type: ignore
    return kb


async def get_users_medias_kb(type: str, user: dict, page: int, per_page=9) -> InlineKeyboardMarkup:
    list_name = type_to_list_name(type)
    media_list = user[list_name]
    last_page = ceil(len(media_list) / per_page) - 1

    kb = InlineKeyboardMarkup()

    for media in media_list[per_page * page: per_page * page + per_page]:
        kb.row(InlineKeyboardButton(text=media["Title"]["userPreferred"],  # type: ignore
                                    callback_data=f"view_user_media_{media['Id']}"))
    if page == 0:
        kb.row(InlineKeyboardButton(text=">",
                                    callback_data=f"view_users_list_{type}_p_{page + 1}"))  # type: ignore
    elif page == last_page:
        kb.row(InlineKeyboardButton(text="<",
                                    callback_data=f"view_users_list_{type}_p_{page - 1}"))  # type: ignore
    else:
        kb.row(InlineKeyboardButton(text="<",
                                    callback_data=f"view_users_list_{type}_p_{page - 1}"),  # type: ignore
               InlineKeyboardButton(text=">",
                                    callback_data=f"view_users_list_{type}_p_{page + 1}"))  # type: ignore
    kb.row(InlineKeyboardButton(
        text="Back", callback_data=f"view_main_menu"))  # type: ignore
    return kb
