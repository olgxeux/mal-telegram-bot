from aiogram import types
from aiogram.filters import Command
from loader import dp
from bot.keyboards.inline_keybords import *
from database.mongodb_manager import create_new_user


@dp.message(Command("start"))
async def start_bot(message: types.Message):
    user_id = message.from_user.id
    await create_new_user(user_id)
    kb = get_main_menu_kb()
    await message.reply("Choose an action:",
                        reply_markup=kb)
