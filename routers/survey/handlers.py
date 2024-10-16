import asyncio

from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from keyboads import (
    get_cancel_button,
    get_confirm_button,
    get_keyboard,
    get_start_keyboard,
)
from settings import settings
from utils import calculate_summ, find_quantity

from .states import Support, Survey

router = Router(name=__name__)

cancel_text = "🚫 Отмена 🚫"


@router.message(F.text == "💎 Покупка гемов 💎")
async def start_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text="Выбери 1 из вариантов или введи свое количество",
        reply_markup=get_keyboard(),
    )
    await state.set_state(Survey.quantity)


@router.message(F.text == "📥 Связаться с поддержкой 📥")
async def support_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text="📝 Напиши свое сообщение админу и он сразу тебе ответит, как освободится 📝",
        reply_markup=get_cancel_button(cancel_text),
    )
    await state.set_state(Support.report)


@router.message(Support.report)
async def report_handler(message: types.Message, state: FSMContext) -> None:
    await message.bot.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgIAAxkBAAEM9x1nDRaGogtRz"
        "n2Pqc3Zsdq6wnavMQACSAIAAladvQoc9XL43CkU0DYE",
    )
    for admin in settings.admin_ids:
        await message.bot.forward_message(
            chat_id=admin,
            from_chat_id=message.chat.id,
            message_id=message.message_id,
        )
        await message.bot.send_message(
            chat_id=admin,
            text=f"{message.chat.id}",
        )

    await message.answer(
        text="📩 Я успешно переслал твое сообщение Админу! 📩",
        reply_markup=get_start_keyboard(),
    )
    await state.clear()


@router.message(F.text.contains("1000 гемов") | F.text.contains("5000 гемов"))
@router.message(F.text.contains("10000 гемов"))
@router.message(F.text.contains("25000 гемов"))
@router.message(F.text.contains("50000 гемов"))
@router.message(F.text.contains("100000 гемов"))
@router.message(F.text.isdigit(), Survey.quantity)
async def quantity_handler(message: types.Message, state: FSMContext) -> None:
    quantity: int = 0
    if isinstance(message.text, str):
        quantity = find_quantity(message.text)
    if quantity > 999:
        price = str(calculate_summ(quantity))
        await state.update_data(quantity=quantity, price=price)
        await state.set_state(Survey.nickname)
        await message.answer(
            text=f"Отлично!\nТы хочешь купить {quantity} шт. за {price} рублей"
        )
        await asyncio.sleep(0.3)
        await message.answer(
            text="Теперь введи свой ник в TDD,"
            " будь внимательнее, туда в Post Office придут гемы",
            reply_markup=get_cancel_button(cancel_text),
        )
    elif quantity < 1000:
        await message.answer(text="⚠️ Минимальное число гемов для покупки - 1000 ⚠️")


@router.message(Survey.quantity)
async def unknown_type_handler(message: types.Message) -> None:
    await message.answer(
        text="Введи число гемов, которое ты хочешь купить, а я посчитаю сумму"
    )


@router.message(F.text, Survey.nickname)
async def nickname_handler(message: types.Message, state: FSMContext) -> None:
    await state.update_data(nickname=message.text)
    data = await state.get_data()
    await message.answer(
        text=f"Осталось только заплатить!\n\n"
        f"💳 Сбербанк: 234234234 💳"
        f"\n💰{data['price']} рублей.💰"
    )
    await message.answer(
        text="Как оплатишь покупку нажми кнопку '😎 Оплатил! 😎'",
        reply_markup=get_confirm_button(cancel_text),
    )
    await state.set_state(Survey.confirm)


@router.message(~F.text, Survey.nickname)
async def invalid_nickname_handler(message: types.Message) -> None:
    await message.answer(
        text="❗️❗️❗️ Введи свой ник из TDD, туда на Post Office придут гемы ❗️❗️❗️",
        reply_markup=get_cancel_button(cancel_text),
    )


@router.message(F.text == "😎 Оплатил! 😎", Survey.confirm)
async def confirm_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text="🎉Спасибо за покупку!🎉\nТовар придет в течение 5 минут, с 08:00 до 23:00",
        reply_markup=get_start_keyboard(),
    )
    await message.bot.send_sticker(
        chat_id=message.chat.id,
        sticker="CAACAgIAAxkBAAEM9x1nDRaGogtRzn2Pqc3"
        "Zsdq6wnavMQACSAIAAladvQoc9XL43CkU0DYE",
    )
    data = await state.get_data()
    for admin in settings.admin_ids:
        await message.bot.send_message(
            chat_id=admin,
            text=f"Nickname TDD: {data['nickname']}\n"
            f"Nickname TG: {message.from_user.username}\n"
            f"User ID: {message.from_user.id}\n"
            f"Количество: {data['quantity']}\n"
            f"К оплате: {data['price']}",
        )
    await state.clear()


@router.message(F.reply_to_message & F.from_user.id.in_(settings.admin_ids))
async def unknown_handler(message: types.Message) -> None:
    for m in message:
        print(m)
    await message.bot.forward_message(
        chat_id=815114488,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
    )


@router.message(F.bot.forward_message)
async def forward_handler(message: types.Message) -> None:
    for m in message:
        print(m)
