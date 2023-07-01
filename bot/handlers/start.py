from aiogram import types
from aiogram.filters import Command
from loader import dp
from bot.keyboards.inline_keybords import *


@dp.message(Command("start"))
async def start_bot(message: types.Message):
    kb = get_main_menu_kb()
    await message.reply("Choose an action:",
                        reply_markup=kb)
