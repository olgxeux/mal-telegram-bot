from aiogram import types
from aiogram.fsm.context import FSMContext


from loader import dp, bot
from bot.keyboards.inline_keybords import get_searching_menu_kb, get_search_medias_kb, get_rating_step_menu_kb, get_status_step_menu_kb, get_users_medias_kb
from bot.message_utils import media_message_params
from bot.callbacks import SearchMediaCB, ViewSearchListCB, ViewSearchMediaCB, ViewAddRatingMenuCB, ViewAddStatusMenuCB, AddMediaCB
from bot.states.search_states import SearchStates
from database.gql_manager import *
from database.mongodb_manager import get_user, add_media_for_user


@dp.callback_query(SearchMediaCB.filter())
async def serch_media(callback: types.CallbackQuery, callback_data: SearchMediaCB, state: FSMContext):
    media_type = callback_data.media_type
    from_page = callback_data.from_page

    kb = await get_searching_menu_kb(media_type, from_page)

    await state.set_state(SearchStates.waiting_for_prompt)
    await state.update_data(media_type=media_type)
    await state.update_data(from_page=from_page)

    await callback.message.edit_text(
        f"What {media_type} are you looking for?",
        reply_markup=kb)


@dp.message(SearchStates.waiting_for_prompt)
async def view_search_list(message: types.Message, state: FSMContext):
    await state.update_data(search_prompt=message.text)
    data = await state.get_data()
    await state.clear()

    search_prompt = data["search_prompt"]
    media_type = data["media_type"]
    from_page = data["from_page"]
    page = (await get_page(1, search_prompt, media_type.upper()))["Page"]
    medias = page["media"]
    has_next_page = page["pageInfo"]["hasNextPage"]

    kb = await get_search_medias_kb(media_type, search_prompt, medias, 0, has_next_page, from_page)

    if message.photo:
        chat_id = message.chat.id
        message_id = message.message_id
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        await bot.send_message(chat_id=chat_id, text=f'Search result for "{search_prompt}":', reply_markup=kb)
    else:
        chat_id = message.chat.id
        message_id = message.message_id
        await bot.send_message(chat_id=chat_id, text=f'Search result for "{search_prompt}":', reply_markup=kb)


@dp.callback_query(ViewSearchListCB.filter())
async def view_users_media_list(callback: types.CallbackQuery, callback_data: ViewSearchListCB):
    # user_id = 228
    user_id = callback.from_user.id
    user = await get_user(user_id)

    search_prompt = callback_data.search_prompt
    media_type = callback_data.media_type
    from_page = callback_data.from_page
    page_number = callback_data.page

    page = (await get_page(page_number, search_prompt, media_type.upper()))["Page"]
    medias = page["media"]
    has_next_page = page["pageInfo"]["hasNextPage"]

    kb = await get_search_medias_kb(media_type, search_prompt, medias, page_number, has_next_page, from_page)

    if callback.message.photo:
        chat_id = callback.message.chat.id
        message_id = callback.message.message_id
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        await bot.send_message(chat_id=chat_id, text=f'Search result for "{search_prompt}":', reply_markup=kb)
    else:
        await callback.message.edit_text(text=f'Search result for "{search_prompt}":',
                                         reply_markup=kb)


@dp.callback_query(ViewSearchMediaCB.filter())
async def view_search_media(callback: types.CallbackQuery, callback_data: ViewSearchMediaCB):
    # user_id = 228
    user_id = callback.from_user.id
    user = await get_user(user_id)

    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page = callback_data.from_page
    search_prompt = callback_data.search_prompt

    image, message_text, kb = await media_message_params(media_type, user, media_id, from_page, search_prompt)

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_photo(chat_id=chat_id, photo=image, caption=message_text, reply_markup=kb)


@dp.callback_query(ViewAddRatingMenuCB.filter())
async def add_rating_media(callback: types.CallbackQuery, callback_data: ViewAddRatingMenuCB):
    # user_id = 228
    user_id = callback.from_user.id
    user = await get_user(user_id)

    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page = callback_data.from_page
    search_prompt = callback_data.search_prompt

    kb = await get_rating_step_menu_kb(
        media_type, media_id, from_page, search_prompt)

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_message(chat_id=chat_id, text="rating", reply_markup=kb)


@dp.callback_query(ViewAddStatusMenuCB.filter())
async def add_status_media(callback: types.CallbackQuery, callback_data: ViewAddStatusMenuCB):
    # user_id = 228
    user_id = callback.from_user.id
    user = await get_user(user_id)

    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page = callback_data.from_page
    search_prompt = callback_data.search_prompt
    rating = callback_data.rating

    kb = await get_status_step_menu_kb(
        media_type, media_id, from_page, rating, search_prompt)

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_message(chat_id=chat_id, text="rating", reply_markup=kb)


@dp.callback_query(AddMediaCB.filter())
async def add_media(callback: types.CallbackQuery, callback_data: AddMediaCB):
    # user_id = 228
    user_id = callback.from_user.id
    user = await get_user(user_id)

    media_type = callback_data.media_type
    media_id = callback_data.media_id
    from_page = callback_data.from_page
    search_prompt = callback_data.search_prompt
    rating = callback_data.rating
    status = callback_data.status

    media = (await get_media(media_id))["Media"]

    user_media = {
        "Id": media_id,
        "Title": media["title"],
        "Rating": str(rating),
        "Status": str(status)
    }
    user = await add_media_for_user(media_type, user_id, user_media)

    image, message_text, kb = await media_message_params(media_type, user, media_id, from_page, search_prompt)

    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await bot.send_photo(chat_id=chat_id, photo=image, caption=message_text, reply_markup=kb)
