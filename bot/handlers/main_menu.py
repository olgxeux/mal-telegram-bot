from aiogram import types
from loader import dp
from bot.keyboards.inline_keybords import get_main_menu_kb
from bot.callbacks import ViewMainMenuCB


@dp.callback_query(ViewMainMenuCB.filter())
async def view_main_menu(callback: types.CallbackQuery):
    kb = get_main_menu_kb()
    await callback.message.edit_text("Choose an action:", reply_markup=kb)
