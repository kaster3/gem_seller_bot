from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart

from keyboads import get_start_keyboard

router = Router(name=__name__)


@router.message(CommandStart())
@router.message(F.text == "🚫 Отмена 🚫")
async def start_handler(message: types.Message) -> None:
    await message.answer(
        text=f"Привет, {message.from_user.first_name}! 👋",
        reply_markup=get_start_keyboard(),
    )


@router.message(Command("help"))
async def help_handler(message: types.Message) -> None:
    await message.answer(
        text="Ты можешь приобрести у меня гемы для TDD по низким ценам",
    )
