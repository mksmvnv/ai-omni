from aiogram.fsm.state import State, StatesGroup


class Generate(StatesGroup):
    text = State()
