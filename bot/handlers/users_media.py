from aiogram import types
from loader import dp, bot
from database.mongodb_manager import get_user, change_users_media_rating
from bot.keyboards.inline_keybords import get_rating_menu_kb
from bot.callbacks import ViewRatingMenuCB, ChangeRatingCB
from bot.message_utils import media_message_params


@dp.callback_query(ViewRatingMenuCB.filter())
async def view_rating_menu(callback: types.CallbackQuery, callback_data: ViewRatingMenuCB):
    user_id = 228
    user = await get_user(user_id)

    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page = callback_data.from_page

    kb = await get_rating_menu_kb(media_type, media_id, from_page)

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_message(chat_id=chat_id, text=f"Choose rating:", reply_markup=kb)


@dp.callback_query(ChangeRatingCB.filter())
async def change_rating(callback: types.CallbackQuery, callback_data: ChangeRatingCB):
    media_type = callback_data.media_type
    media_id = callback_data.media_id
    rating = callback_data.rating
    from_page = callback_data.from_page
# type to int
    user_id = 228
    user = await change_users_media_rating(media_type, user_id, media_id, str(rating))

    image, message_text, kb = await media_message_params(media_type, user, media_id, from_page)

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_photo(chat_id=chat_id, photo=image, caption=message_text, reply_markup=kb)
