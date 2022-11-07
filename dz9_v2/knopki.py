from aiogram import Bot, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = types.ReplyKeyboardMarkup(resize_keyboard=True)

pole1 = types.KeyboardButton('1')
pole2 = types.KeyboardButton('2')
pole3 = types.KeyboardButton('3')
pole4 = types.KeyboardButton('4')
pole5 = types.KeyboardButton('5')
pole6 = types.KeyboardButton('6')
pole7 = types.KeyboardButton('7')
pole8 = types.KeyboardButton('8')
pole9 = types.KeyboardButton('9')

start.add(pole1, pole2, pole3, pole4, pole5, pole6, pole7, pole8, pole9)