from aiogram.types import Message
from aiogram import types

from loader import dp
from utils import photo_link

import pytesseract
from PIL import Image

from transliterate import to_cyrillic, to_latin

from keyboards.default.langMenu import menuStart

import urllib.request


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    # await msg.answer(link)
    urllib.request.urlretrieve(link, "image.png")
    await msg.reply(" Matning tilini tanlang : ", reply_markup=menuStart)


@dp.message_handler(text_contains="uz")
async def select_lang(msg:Message):
    img = Image.open("image.png")
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    text = pytesseract.image_to_string(img, lang="uzb")
    # print(text)
    #await msg.answer(text)

    await msg.answer(to_cyrillic(text))

    await msg.answer(to_latin(text))

@dp.message_handler(text_contains="ru")
async def select_lang(msg:Message):
    img = Image.open("image.png")
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    text = pytesseract.image_to_string(img, lang="rus")
    # print(text)
    #await msg.answer(text)

    await msg.answer(to_cyrillic(text))

    await msg.answer(to_latin(text))

@dp.message_handler(text_contains="eng")
async def select_lang(msg:Message):
    img = Image.open("image.png")
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    text = pytesseract.image_to_string(img, lang="eng")
    # print(text)
    #await msg.answer(text)

    await msg.answer(to_cyrillic(text))

    await msg.answer(to_latin(text))



