import re
from urllib import request
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



menuCategory  =  ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="👨‍🎓 Talaba"),
            KeyboardButton(text="👨‍👩‍👧 Ota ona"),
        ],
        [
            KeyboardButton(text="👨‍💼 Xodimlar"),
            KeyboardButton(text="Boshqa"),
        ],
        
    ],
    resize_keyboard=True,
)


murojat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1.Shikoyat", callback_data="shikoyat"),
            KeyboardButton(text="2.Taklif", callback_data="taklif"),

        ],
        [
            KeyboardButton(text="3.Ariza", callback_data="ariza"),
            KeyboardButton(text="4.Boshqa", callback_data="boshqa"),
        ],
        
    ],
    resize_keyboard=True
)


orqaga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start"),
        ]
    ],
    resize_keyboard=True


)


check_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tekshirish"),
        ]
    ],
    resize_keyboard=True


)

my_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telofon raqam",
            request_contact=True)
        ]
    ],
    resize_keyboard=True
)