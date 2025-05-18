from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from keyboards.user_keyboard import *
from parser.news_pars import get_rbc_news
from parser.weather_pars import get_weather



router = Router()




@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(f'Привет! {message.from_user.first_name}\n'
                         f'Выбери действие', reply_markup=main)




@router.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer('Этот бот преднезначен\n'
                         'для показа текущей погоды\n'
                         'и последних новостей')


@router.message(F.text == '📰 Последние новости')
async def news_cmd(message: Message):
    news = await get_rbc_news()
    text = '📰 Последние новости:\n\n' + '\n'.join(news)

    await message.answer(text)


@router.message(F.text == '⚙️ Настройки')
async def settings_cmd(message: Message):
    await message.answer('Выбери действие', reply_markup=settings)


@router.callback_query(F.data.in_(['vkluchit', 'vikluchit']))
async def vkluchenie_cmd(callback: CallbackQuery):
    if callback.data == 'vkluchit':
        await callback.message.edit_text('Уведомления включены')
    elif callback.data == 'vikluchit':
        await callback.message.edit_text('Уведомления выключены')





@router.message(F.text == '🌡️ Узнать погоду')
async def weather_cmd(message: Message):
    await message.answer('Введите название города')





@router.message()
async def get_weather_cmd(message: Message):
    city = message.text.strip()
    weather_info = await get_weather(city)
    await message.reply(weather_info)















