from aiogram import types
from loader import dp, bot
from bot.keyboards.inline_keybords import get_users_medias_kb
from bot.message_utils import media_message_params
from bot.callbacks import ViewUsersListCB, ViewUsersMediaCB
from database.gql_manager import *
from database.mongodb_manager import get_user


@dp.callback_query(ViewUsersListCB.filter())
async def view_users_media_list(callback: types.CallbackQuery, callback_data: ViewUsersListCB):
    user_id = 228
    user = await get_user(user_id)

    type = callback_data.media_type
    page = callback_data.page
    kb = await get_users_medias_kb(type, user, page)

    # if callback_data.media_type:
    if callback.message.photo:
        chat_id = callback.message.chat.id
        message_id = callback.message.message_id
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        await bot.send_message(chat_id=chat_id, text=f"Here is your {type} list:", reply_markup=kb)
    else:
        await callback.message.edit_text(f"Here is your {type} list:",
                                         reply_markup=kb)


@dp.callback_query(ViewUsersMediaCB.filter())
async def view_users_media(callback: types.CallbackQuery, callback_data: ViewUsersMediaCB):
    user_id = 228
    user = await get_user(user_id)

    # print(callback.data)
    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page = callback_data.from_page

    image, message_text, kb = await media_message_params(media_type, user, media_id, from_page)

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_photo(chat_id=chat_id, photo=image, caption=message_text, reply_markup=kb)
