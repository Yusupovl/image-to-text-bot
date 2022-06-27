from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🇺🇿uz'),
            KeyboardButton(text="🇷🇺ru"),
            KeyboardButton(text="🇬🇧eng"),
            KeyboardButton(text="🇺🇿🇷🇺kiril"),
        ],
    ],
    resize_keyboard=True
)