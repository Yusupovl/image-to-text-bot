from aiogram import types
from aiogram.types import ContentType,Message
from loader import dp

import pytesseract
from PIL import Image


# Echo bot
@dp.message_handler(content_types='photo')
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    # await message.reply("Rasim qabul qilindi\n"
    #                     f"file_id = {message.photo[-1].file_id}")
    # //foto_id = message.photo[-1].file_id
    img = Image.open("slide-0.jpg")
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    text = pytesseract.image_to_string(img,lang="rus")
    print(text)
    await message.answer(text)


