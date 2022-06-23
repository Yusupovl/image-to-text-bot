import logging

from aiogram.types import  Message
from loader import dp
from keyboards.inline.inlineKeyboard import language

@dp.message_handler(content_types='photo')
async def select_category(message: Message):
    await message.answer(f"Tilni tanlang",reply_markup=language)