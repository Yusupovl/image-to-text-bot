import logging
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.builtin import Text


from keyboards.default.startMenu import menuStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    logging.info(f"{message.from_user.id=}")
    logging.info(f"{message.from_user.full_name=}")
    users = {message.from_user.id:message.from_user.username}
    print(users)
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("rasmni yuboring:  ")





# @dp.message_handler(Text(contains='axmoq',ignore_case=True))
# async def text_example(msg:types.Message):
#     #await msg.reply_video(msg.chat.id, open(1257602754, 'rb'))


