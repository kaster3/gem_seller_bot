from aiogram.utils.keyboard import (
    KeyboardButton,
    ReplyKeyboardBuilder,
    ReplyKeyboardMarkup,
)


def get_keyboard() -> ReplyKeyboardMarkup:
    names = (
        "💎 1000 гемов(0.035р за шт) - 35р 💎",
        "💎 5000 гемов(0.033р за шт) - 150р 💎",
        "💎 10000 гемов(0.03р за шт) - 270р 💎",
        "💎 25000 гемов(0.027р за шт) - 625р 💎",
        "💎 50000 гемов(0.025р за шт) - 1250р 💎",
        "💎 100000 гемов(0.020р за шт) - 2000р 💎",
    )

    builder = ReplyKeyboardBuilder()

    for name in names:
        builder.button(text=name)

    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)


def get_confirm_button(cancel_txt: str) -> ReplyKeyboardMarkup:
    confirm_text = "😎 Оплатил! 😎"
    builder = ReplyKeyboardBuilder()
    builder.button(text=confirm_text)
    builder.button(text=cancel_txt)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def get_start_keyboard() -> ReplyKeyboardMarkup:
    gem_button = [KeyboardButton(text="💎 Покупка гемов 💎")]
    support_button = [KeyboardButton(text="📥 Связаться с поддержкой 📥")]
    return ReplyKeyboardMarkup(
        keyboard=[
            gem_button,
            support_button,
        ],
        resize_keyboard=True,
    )


def get_cancel_button(cancel_txt: str) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=cancel_txt)
    return builder.as_markup(resize_keyboard=True)


def get_menu_button(main_txt: str) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=main_txt)
    return builder.as_markup(resize_keyboard=True)
