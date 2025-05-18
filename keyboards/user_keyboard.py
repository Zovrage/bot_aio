from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Основная Reply-клавиатура
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🌡️ Узнать погоду'), KeyboardButton(text='📰 Последние новости')],
    [KeyboardButton(text='⚙️ Настройки')]

], resize_keyboard=True)


# Inline-клавиатура для настройки
settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Включить', callback_data='vkluchit'),
     InlineKeyboardButton(text='Выключить', callback_data='vikluchit')]
])