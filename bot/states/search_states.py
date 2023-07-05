from aiogram.fsm.state import State, StatesGroup


class SearchStates(StatesGroup):
    waiting_for_prompt = State()
