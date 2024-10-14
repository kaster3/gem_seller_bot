from aiogram.fsm.state import State, StatesGroup


class Survey(StatesGroup):
    quantity = State()
    nickname = State()
    confirm = State()
    price: int = 0


class Support(StatesGroup):
    report = State()
