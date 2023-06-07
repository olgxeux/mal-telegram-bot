from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStates(StatesGroup):
    main_menu = State()
    users_media_list = State()
    users_media = State()
