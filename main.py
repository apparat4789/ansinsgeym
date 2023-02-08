import asyncio
import json
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.utils import executor
import markups as nav
from db import Database
from aiogram.contrib.fsm_storage.memory import MemoryStorage




logging.basicConfig(level=logging.INFO)
bot = Bot(token="6157672241:AAF03Ir9EY1Sd98PfJ2G8ePVIeY9FfaDOYs")
dp = Dispatcher(bot, storage=MemoryStorage())

db = Database()


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    if(not db.users_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await message.answer("Назови свое имя странник")
        pass
    else:
        await message.answer( "Вы уже зарегистрированы.", reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == 'ПРОФИЛЬ':
            pass

        else:
            if db.get_signup(message.from_user.id) == "setname":
                if(len(message.text) > 15):
                    await message.answer("Слишком длинное имя, я не смогу его запомнить")
                elif '@' in message.text or '/' in message.text:
                    await message.answer("Я не понимаю этих символов")
                else:
                    db.set_name(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, "Понял")
                    await message.answer("Я тебя запомнил, я глаза твои запомнил", reply_markup=nav.mainMenu)
            else:
                await message.answer('Чего блять?')


@dp.message_handler()
async def courses(message: types.Message):
    with open("result.json.json", mode="r", encoding="utf-8") as file:
        flag = True
        list_corses = json.loads(file.read())
        for item in list_corses:
            words = list(item['code'].split(' '))
            if message.text.lower() in words or message.text == item['code']:
                flag = False
                await message.answer(f'{item["code"]}: {item["union"]}')
        if flag:
            await message.answer('Пожалуйста проверьте вводимые данные!')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)


