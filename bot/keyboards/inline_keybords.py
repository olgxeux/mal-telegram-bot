from math import ceil
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
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

    if page > last_page:
        page = last_page

    print(page, last_page)

    builder = InlineKeyboardBuilder()

    if page == -1:
        page = 0

    for media in media_list[per_page * page: per_page * page + per_page]:
        builder.row(
            InlineKeyboardButton(text=media["Title"]["userPreferred"], callback_data=ViewUsersMediaCB(
                media_type=type, media_id=media["Id"], from_page_user=page).pack())
        )

    if last_page != -1 and len(media_list) > per_page:
        if page == 0:
            builder.row(
                InlineKeyboardButton(text=">", callback_data=ViewUsersListCB(media_type=type, page=page + 1).pack()))
        elif page == last_page:
            builder.row(
                InlineKeyboardButton(text="<", callback_data=ViewUsersListCB(media_type=type, page=page - 1).pack()))
        else:
            builder.row(
                InlineKeyboardButton(text="<", callback_data=ViewUsersListCB(
                    media_type=type, page=page - 1).pack()),
                InlineKeyboardButton(text=">", callback_data=ViewUsersListCB(
                    media_type=type, page=page + 1).pack())
            )

    builder.row(InlineKeyboardButton(
        text="Back", callback_data=ViewMainMenuCB().pack()))
    builder.button(
        text=f"Search {type}",
        callback_data=SearchMediaCB(media_type=type, from_page_user=page))

    return builder.as_markup()


async def get_users_media_kb(type: str, media: dict, from_page_user: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    media_id = media['id']

    builder.row(InlineKeyboardButton(
        text="Change rating",
        callback_data=ViewRatingMenuCB(media_type=type, media_id=media_id, from_page_user=from_page_user).pack()))

    builder.row(InlineKeyboardButton(
        text="Change status",
        callback_data=ViewStatusMenuCB(media_type=type, media_id=media_id, from_page_user=from_page_user).pack()))

    builder.row(InlineKeyboardButton(
        text="Remove",
        callback_data=ViewRemovingMenuCB(media_type=type, media_id=media_id, from_page_user=from_page_user).pack()))

    builder.row(InlineKeyboardButton(
        text="Back",
        callback_data=ViewUsersListCB(media_type=type, page=from_page_user).pack()))

    return builder.as_markup()


async def get_rating_menu_kb(type: str, media_id: int, from_page_user: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for rating in range(11):
        builder.button(
            text=f"{rating}",
            callback_data=ChangeRatingCB(media_type=type, media_id=media_id, rating=rating, from_page_user=from_page_user))

    builder.button(
        text="Cancel",
        callback_data=ViewUsersMediaCB(media_type=type, media_id=media_id, from_page_user=from_page_user))

    return builder.as_markup()


async def get_status_menu_kb(type: str, media_id: int, from_page_user: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for status in range(4):
        builder.button(
            text=f"{status}",
            callback_data=ChangeStatusCB(media_type=type, media_id=media_id, status=status, from_page_user=from_page_user))

    builder.button(
        text="Cancel",
        callback_data=ViewUsersMediaCB(media_type=type, media_id=media_id, from_page_user=from_page_user))

    return builder.as_markup()


async def get_removing_menu_kb(type: str, media_id: int, from_page_user: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Remove",
        callback_data=RemoveMediaCB(media_type=type, media_id=media_id, from_page_user=from_page_user))
    builder.button(
        text="Cancel",
        callback_data=ViewUsersMediaCB(media_type=type, media_id=media_id, from_page_user=from_page_user))

    return builder.as_markup()


async def get_searching_menu_kb(type: str, from_page_user: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Cancel",
        callback_data=ViewUsersListCB(media_type=type, page=from_page_user))

    return builder.as_markup()


async def get_search_medias_kb(media_type: str, search_prompt: str, media_list: dict, page: int, has_next_page: bool, from_page_user: int, per_page=10) -> InlineKeyboardMarkup:
    last_page = ceil(len(media_list) / per_page) - 1
    if page > last_page:
        page = last_page

    if page == -1:
        page = 0

    builder = InlineKeyboardBuilder()
    for media in media_list[per_page * page: per_page * page + per_page]:
        builder.row(
            InlineKeyboardButton(
                text=media["title"]["userPreferred"],
                callback_data=ViewSearchMediaCB(
                    media_type=media_type,
                    media_id=media["id"],
                    from_page_user=from_page_user,
                    from_page_search=page,
                    search_prompt=search_prompt,).pack(),
            )
        )

    if last_page != -1 and len(media_list) > per_page:
        if page == 0:
            builder.row(
                InlineKeyboardButton(
                    text=">",
                    callback_data=ViewSearchListCB(
                        media_type=media_type,
                        page=page + 1,
                        search_prompt=search_prompt,
                        from_page_user=from_page_user,).pack(),
                )
            )
        elif page == last_page:
            builder.row(
                InlineKeyboardButton(
                    text="<",
                    callback_data=ViewSearchListCB(
                        media_type=media_type,
                        page=page - 1,
                        search_prompt=search_prompt,
                        from_page_user=from_page_user,).pack(),
                )
            )
        else:
            builder.row(
                InlineKeyboardButton(
                    text="<",
                    callback_data=ViewSearchListCB(
                        media_type=media_type,
                        page=page - 1,
                        search_prompt=search_prompt,
                        from_page_user=from_page_user,).pack(),
                ),
                InlineKeyboardButton(
                    text=">",
                    callback_data=ViewSearchListCB(
                        media_type=media_type,
                        page=page + 1,
                        search_prompt=search_prompt,
                        from_page_user=from_page_user,).pack(),
                ),
            )

    builder.row(
        InlineKeyboardButton(
            text="Back",
            callback_data=ViewUsersListCB(
                media_type=media_type, page=from_page_user).pack(),
        ),
        InlineKeyboardButton(
            text=f"Search again",
            callback_data=SearchMediaCB(
                media_type=media_type, from_page_user=from_page_user).pack(),
        ),
    )

    return builder.as_markup()


async def get_search_media_kb(media_type: str, media: dict, from_page_user: int, from_page_search: int, search_prompt: str | None) -> InlineKeyboardMarkup:

    builder = InlineKeyboardBuilder()

    media_id = media['id']
    builder.button(
        text="Add",
        callback_data=ViewAddRatingMenuCB(media_type=media_type, media_id=media_id, from_page_user=from_page_user, from_page_search=from_page_search, search_prompt=search_prompt))
    builder.button(
        text="Back",
        callback_data=ViewSearchListCB(search_prompt=search_prompt, media_type=media_type, page=from_page_search, from_page_user=from_page_user))
    print(search_prompt)

    return builder.as_markup()



async def get_users_media_in_search_kb(media_type: str, media: dict, from_page_user: int, from_page_search: int, search_prompt: str | None) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    media_id = media['id']


    builder.row(InlineKeyboardButton(
        text="View in your list",
        callback_data=ViewUsersMediaCB(media_type=media_type, media_id=media_id, from_page_user=0).pack()))

    builder.row(InlineKeyboardButton(
        text="Back",
        callback_data=ViewSearchListCB(search_prompt=search_prompt, media_type=media_type, page=from_page_search, from_page_user=from_page_user).pack()))

    return builder.as_markup()




async def get_rating_step_menu_kb(type: str, media_id: int, from_page_user: int, from_page_search: int, search_prompt: str | None) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for rating in range(11):
        builder.button(
            text=f"{rating}",
            callback_data=ViewAddStatusMenuCB(media_type=type, media_id=media_id, rating=rating, from_page_user=from_page_user, from_page_search=from_page_search, search_prompt=search_prompt))

    builder.button(
        text="Cancel",
        callback_data=ViewUsersMediaCB(media_type=type, media_id=media_id, from_page_user=from_page_user, from_page_search=from_page_search, search_prompt=search_prompt))

    return builder.as_markup()


async def get_status_step_menu_kb(type: str, media_id: int, from_page_user: int, rating: int, search_prompt: str, from_page_search: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for status in range(4):
        builder.button(
            text=f"{status}",
            callback_data=AddMediaCB(media_type=type, media_id=media_id, rating=rating, status=status, from_page_user=from_page_user, search_prompt=search_prompt, from_page_search=from_page_search))

    builder.button(
        text="Cancel",
        callback_data=ViewUsersMediaCB(media_type=type, media_id=media_id, from_page_user=from_page_user, from_page_search=from_page_search, search_prompt=search_prompt))

    return builder.as_markup()
