from aiogram import Bot, Dispatcher, types , executor
import random
from config import token


bot = Bot(token=token)
dp = Dispatcher(bot)
text = random.randint(1,3)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('Я загадал число между 1 и 3, попробуй гадать')

@dp.message_handler(text = '1')
async def start(message:types.Message):
    if text == 1:
        await message.answer('Вы выиграли')
    
    elif text != 1:
        await message.answer('Вы проиграли')
        

@dp.message_handler(text = '2')
async def start(message:types.Message):
    if text == 2:
        await message.answer('Вы выиграли')
        
    elif text!= 2:
        await message.reply('Вы проиграли')
        
@dp.message_handler(text = '3')
async def start(message:types.Message):
    if text == 3:
        await message.reply('Вы выиграли')

    elif text != 3:
        await message.reply('Вы проиграли')

executor.start_polling(dp)
