
from distutils.log import INFO
from fileinput import filename, lineno
from this import d
from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
import logging
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State



from confyg import TOKEN
import knopki

import logging  # вывод информации в консоль о запуске бота


storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(format=u'%(filenames)s [LINE:(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    )


@dp.message_handler(commands=('start'), state = None)
async def process_start_command(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text = '1'),
            types.KeyboardButton(text = '2'),
            types.KeyboardButton(text = '3'),
            types.KeyboardButton(text = '4'),
            types.KeyboardButton(text = '5'),
            types.KeyboardButton(text = '6'),
            types.KeyboardButton(text = '7'),
            types.KeyboardButton(text = '8'),
            types.KeyboardButton(text = '9')
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='Введите номер поля (от 1 до 9)')
    ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    await message.answer("Выберите поле", reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("выберите поле от 1 до 9!")

@dp.message_handler()
async def pole(message: types.Message):
    #kib = '1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9'
    kib = [['1', '2', '3'],
           ['4', '5', '6'],
           ['7', '8', '9']]
    # case:
    #     types.KeyboardButton = '1'
    
    
    await message.reply(f'{",".join(kib[0])}\n{" ".join(kib[1])}\n{" ".join(kib[2])}')
    


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)




if __name__ == '__main__':
    executor.start_polling(dp)
    #@dp.message_handler()



# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types

# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = Bot(token="свой токен")
# # Диспетчер
# dp = Dispatcher(bot)

# # Хэндлер на команду /start
# @dp.message_handler(commands=["start", 'Hello'])
# async def cmd_start(message: types.Message):
# await message.answer("Hello!")

# # Запуск процесса поллинга новых апдейтов
# async def main():
# await dp.start_polling(bot)

# if __name__ == "__main__":
# asyncio.run(main())
# Юрий(Преподаватель): https://pastebin.com/7tjLgwQe
# Юрий(Преподаватель): https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html
# Юрий(Преподаватель): https://tproger.ru/articles/telegram-bot-create-and-deploy/
# Юрий(Преподаватель): https://mastergroosha.github.io/aiogram-3-guide/quickstar