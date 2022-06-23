from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import lang_callback

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="uz",callback_data="uzb"),
            InlineKeyboardButton(text="ru",callback_data="rus"),
            InlineKeyboardButton(text="eng",callback_data="eng"),
        ],
    ])

# language = InlineKeyboardMarkup(row_width=1)
# python = InlineKeyboardButton(text="Uzbek",callback_data=lang_callback.new(item_name="python"))
# language.insert(python)