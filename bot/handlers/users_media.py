from aiogram import types
from loader import dp, bot
from database.mongodb_manager import get_user, change_users_media_rating, change_users_media_status, remove_media_from_user
from bot.keyboards.inline_keybords import get_rating_menu_kb, get_status_menu_kb, get_removing_menu_kb, get_users_medias_kb
from bot.callbacks import ViewRatingMenuCB, ChangeRatingCB, ViewStatusMenuCB, ChangeStatusCB, ViewRemovingMenuCB, RemoveMediaCB
from bot.message_utils import media_message_params


@dp.callback_query(ViewRatingMenuCB.filter())
async def view_rating_menu(callback: types.CallbackQuery, callback_data: ViewRatingMenuCB):
    # user_id = 228
    user_id = callback.from_user.id
    user = await get_user(user_id)

    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page_user = callback_data.from_page_user

    kb = await get_rating_menu_kb(media_type, media_id, from_page_user)

    chat_id = callback.message.chat.id  # type: ignore
    message_id = callback.message.message_id  # type: ignore
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_message(chat_id=chat_id, text=f"Choose rating:", reply_markup=kb)


@dp.callback_query(ChangeRatingCB.filter())
async def change_rating(callback: types.CallbackQuery, callback_data: ChangeRatingCB):
    media_type = callback_data.media_type
    media_id = callback_data.media_id
    rating = callback_data.rating
    from_page_user = callback_data.from_page_user
# type to int
    # user_id = 228
    user_id = callback.from_user.id
    user = await change_users_media_rating(media_type, user_id, media_id, str(rating))

    image, message_text, kb = await media_message_params(media_type, user, media_id, from_page_user)

    chat_id = callback.message.chat.id  # type: ignore
    message_id = callback.message.message_id  # type: ignore
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_photo(chat_id=chat_id, photo=image, caption=message_text, reply_markup=kb)


@dp.callback_query(ViewStatusMenuCB.filter())
async def view_status_menu(callback: types.CallbackQuery, callback_data: ViewStatusMenuCB):
    # user_id = 228
    user_id = callback.from_user.id
    user = await get_user(user_id)

    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page_user = callback_data.from_page_user

    kb = await get_status_menu_kb(media_type, media_id, from_page_user)

    chat_id = callback.message.chat.id  # type: ignore
    message_id = callback.message.message_id  # type: ignore
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_message(chat_id=chat_id, text=f"Choose status:", reply_markup=kb)


@dp.callback_query(ChangeStatusCB.filter())
async def change_status(callback: types.CallbackQuery, callback_data: ChangeStatusCB):
    media_type = callback_data.media_type
    media_id = callback_data.media_id
    status = callback_data.status
    from_page_user = callback_data.from_page_user
# type to int
    # user_id = 228
    user_id = callback.from_user.id
    user = await change_users_media_status(media_type, user_id, media_id, str(status))

    image, message_text, kb = await media_message_params(media_type, user, media_id, from_page_user)

    chat_id = callback.message.chat.id  # type: ignore
    message_id = callback.message.message_id  # type: ignore
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_photo(chat_id=chat_id, photo=image, caption=message_text, reply_markup=kb)


@dp.callback_query(ViewRemovingMenuCB.filter())
async def view_removing_menu(callback: types.CallbackQuery, callback_data: ViewRemovingMenuCB):
    # user_id = 228
    user_id = callback.from_user.id
    user = await get_user(user_id)

    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page_user = callback_data.from_page_user

    kb = await get_removing_menu_kb(media_type, media_id, from_page_user)

    chat_id = callback.message.chat.id  # type: ignore
    message_id = callback.message.message_id  # type: ignore
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_message(chat_id=chat_id, text=f"Are you sure?", reply_markup=kb)


@dp.callback_query(RemoveMediaCB.filter())
async def remove_media(callback: types.CallbackQuery, callback_data: RemoveMediaCB):
    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page_user = callback_data.from_page_user
# type to int
    # user_id = 228
    user_id = callback.from_user.id
    user = await remove_media_from_user(media_type, user_id, media_id)

    kb = await get_users_medias_kb(media_type, user, from_page_user)

    await callback.message.edit_text(f"Here is your {media_type} list:", reply_markup=kb)
