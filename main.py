from aiogram import types,executor,Bot,Dispatcher
from config import token
from search_info import search_info

bot=Bot(token=token)
dp=Dispatcher(bot)
mode="Markdown"

@dp.message_handler(commands="start")
async def start(message:types.Message):
    await bot.send_message(message.chat.id,"*Xush kelibsiz,maqola nomini kiriting*",parse_mode=mode)

@dp.message_handler(content_types="text",chat_type="private")
async def text(message:types.Message):
    response=search_info(message.text)
    await bot.send_message(message.chat.id,f"*{response}*",parse_mode=mode)

executor.start_polling(dp,skip_updates=True)