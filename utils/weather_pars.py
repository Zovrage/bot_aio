import aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



async def get_weather(city: str):
    url = f"https://pogoda.mail.ru/prognoz/{city.lower()}/"
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            data = soup.find('div', {'data-logger-parent': 'content'})

            temperature = data.find('div', {'data-qa': 'Title'}).text.strip()

            description = soup.find('div', {'data-logger': 'pogoda__MainForecastToday'}).find('div', {'data-qa': 'Text'}, class_='c3132db061 fd517a8fd5').text.strip()

    return f'{temperature}\n {description}'


