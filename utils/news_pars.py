import asyncio
import aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



async def get_rbc_news():
    url = 'https://www.rbc.ru/'
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            data = soup.find('div', class_='l-col-main__inner').find('section', class_='main js-main-reload')

            news = data.find_all('div', class_='tabs__item js-index-tabs')

            news_items = []

            for i in news:
                links = i.find('a', class_='tabs__link').get('href')
                news_items.append(links)


            return news_items




