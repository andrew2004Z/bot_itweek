from audioop import ratecv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from sql import WorkDB
from functions import *

from config import TOKEN, ADMIN_ID


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = WorkDB('db.db')
a = '''UhxPb*EW@1%3
3iGgwmFC3p~U
HZBIuo7$YnrT
IlYY0aDKOSIN
8OOXhH*jMVX@
UJT*|XDhokjd
~6ga0Ec6Z|Ji
w%Zdm09@fpDe
|{c1|aX3*PfO
#a9w67ir#}TL'''.split()
print(a)
@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    if db.check_user(msg.from_user.id) == False:
        db.create_user(msg.from_user.id, msg.from_user.username, 0)
        db.create_answer(msg.from_user.id, str(a))
    await msg.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['static'])
async def process_start_command(msg: types.Message):
    if msg.from_user.id in ADMIN_ID:
        raiting = db.get_top_rating()
        raiting = sort_rating(raiting)
        sp = []
        for i in raiting:
            sp.append(f'{i[1]} : {i[2]}')
        await bot.send_message(msg.from_user.id, '\n'.join(sp))
        print(db.ge)
    else:
        await msg.reply("Извините, похоже вы не админ.")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)