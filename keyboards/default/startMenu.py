from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='rasm➡matn'),
            KeyboardButton(text="rasm➡matn➡tarjima"),
        ],
    ],
    resize_keyboard=True
)