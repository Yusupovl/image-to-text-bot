from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Rasmli ma'lumotni matn formatiga o'tkazish uchun botga rasmni yuborishingiz va kerakli tilni tanlashingiz  kifoya: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
