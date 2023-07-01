from math import ceil
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.callbacks import *
from utils import type_to_list_name


def get_main_menu_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="My anime",
        callback_data=ViewUsersListCB(media_type="anime", page=0))
    builder.button(
        text="My manga",
        callback_data=ViewUsersListCB(media_type="manga", page=0))

    return builder.as_markup()


async def get_users_medias_kb(type: str, user: dict, page: int, per_page=9) -> InlineKeyboardMarkup:
    list_name = type_to_list_name(type)
    media_list = user[list_name]
    last_page = ceil(len(media_list) / per_page) - 1

    builder = InlineKeyboardBuilder()

    for media in media_list[per_page * page: per_page * page + per_page]:
        builder.button(
            text=media["Title"]["userPreferred"],
            callback_data=ViewUsersMediaCB(media_type=type, media_id=media["Id"], from_page=page))
    if page == 0:
        builder.button(
            text=">",
            callback_data=ViewUsersListCB(media_type=type, page=page + 1))
    elif page == last_page:
        builder.button(
            text="<",
            callback_data=ViewUsersListCB(media_type=type, page=page - 1))
    else:
        builder.button(
            text="<",
            callback_data=ViewUsersListCB(media_type=type, page=page - 1))
        builder.button(
            text=">",
            callback_data=ViewUsersListCB(media_type=type, page=page + 1))
    builder.button(
        text="Back",
        callback_data=ViewMainMenuCB())

    return builder.as_markup()


async def get_media_kb(type: str, is_in_users_list: bool, media: dict, from_page: int) -> InlineKeyboardMarkup:

    builder = InlineKeyboardBuilder()

    media_id = media['id']
    if is_in_users_list:
        builder.button(
            text="Change rating",
            callback_data=ViewRatingMenuCB(media_id=media_id))
        builder.button(
            text="Change status",
            callback_data=ViewStatusMenuCB(media_id=media_id))
        builder.button(
            text="Remove",
            callback_data=ViewRemovingMenuCB(media_id=media_id))
    else:
        builder.button(
            text="Add",
            callback_data=ViewAddingMenuCB(media_id=media_id))

    builder.button(
        text="Back",
        callback_data=ViewUsersListCB(media_type=type, page=from_page))

    return builder.as_markup()
