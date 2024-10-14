from aiogram.utils.keyboard import (
    KeyboardButton,
    ReplyKeyboardBuilder,
    ReplyKeyboardMarkup,
)


def get_keyboard() -> ReplyKeyboardMarkup:
    names = (
        "1000 гемов(0.035р за шт) - 35р",
        "5000 гемов(0.033р за шт) - 165р",
        "10000 гемов(0.03р за шт) - 300р",
        "25000 гемов(0.027р за шт) - 675р",
        "📥 Связаться с поддержкой 📥",
    )

    last_button = [KeyboardButton(text=names[-1])]

    builder = ReplyKeyboardBuilder()

    for name in names[:-1]:
        builder.button(text=name)

    builder.adjust(2)
    builder.row(last_button[0])

    return builder.as_markup(resize_keyboard=True)


def get_support_button() -> ReplyKeyboardMarkup:
    support_button = [KeyboardButton(text="📥 Связаться с поддержкой 📥")]
    cancel_button = [KeyboardButton(text="🚫 Отмена 🚫")]
    return ReplyKeyboardMarkup(
        keyboard=[support_button, cancel_button],
        resize_keyboard=True,
    )


def get_confirm_button() -> ReplyKeyboardMarkup:
    confirm_button = [KeyboardButton(text="😎 Оплатил! 😎")]
    support_button = [KeyboardButton(text="📥 Связаться с поддержкой 📥")]
    cancel_button = [KeyboardButton(text="🚫 Отмена 🚫")]
    return ReplyKeyboardMarkup(
        keyboard=[confirm_button, support_button, cancel_button],
        resize_keyboard=True,
    )


def get_start_keyboard() -> ReplyKeyboardMarkup:
    gem_button = [KeyboardButton(text="💎 Покупка гемов 💎")]
    return ReplyKeyboardMarkup(
        keyboard=[gem_button],
        resize_keyboard=True,
    )
