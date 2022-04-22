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
answer = ['UhxPb*EW@1%3', '3iGgwmFC3p~U', 'HZBIuo7$YnrT', 'IlYY0aDKOSIN', '8OOXhH*jMVX@', 'UJT*|XDhokjd', '~6ga0Ec6Z|Ji', 'w%Zdm09@fpDe', '|{c1|aX3*PfO', '#a9w67ir#}TL']
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
        for j, i in enumerate(raiting):
            if str(i[2]) != '0':
                sp.append(f'{j}. {i[1]} : {i[2]}')
        await bot.send_message(msg.from_user.id, '\n'.join(sp))
        #print(db.ge)
    else:
        await msg.reply("Извините, похоже вы не админ.")

@dp.message_handler()
async def echo_message(msg: types.Message):
    a = db.get_users_train(msg.from_user.id)[3:-3].split("', '")
    print(a)
    if msg.text in a:
        db.update_score(msg.from_user.id)
        a.remove(msg.text)
        db.update_answer(msg.from_user.id, a)
        await bot.send_message(msg.from_user.id, f'{msg.text} : парвильный ответ \n У вас {db.get_score(msg.from_user.id)} очков.')
    elif msg.text in answer:
        await bot.send_message(msg.from_user.id, f'{msg.text} : парвильный ответ, но вы уже его вводили. \nУ вас {db.get_score(msg.from_user.id)} очков.')
    else:
        await bot.send_message(msg.from_user.id, f'{msg.text} : не является ответом')

if __name__ == '__main__':
    executor.start_polling(dp)