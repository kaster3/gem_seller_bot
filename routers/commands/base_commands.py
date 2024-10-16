from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from keyboads import get_start_keyboard
from settings import settings

router = Router(name=__name__)


@router.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text=f"Привет, {message.from_user.first_name}! 👋",
        reply_markup=get_start_keyboard(),
    )
    if state:
        await state.clear()
    for admin in settings.admin_ids:
        await message.bot.send_message(
            chat_id=admin,
            text=f"{message.from_user.username} начал использовать бота.",
        )


@router.message(Command("help"))
async def help_handler(message: types.Message) -> None:
    await message.answer(
        text="Ты можешь приобрести у меня гемы для TDD по низким ценам",
    )


@router.message((F.text == "🚫 Отмена 🚫") | (F.text == "↪️Главное меню ↩️"))
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text="Ты снова в главном меню!",
        reply_markup=get_start_keyboard(),
    )
    if state:
        await state.clear()
