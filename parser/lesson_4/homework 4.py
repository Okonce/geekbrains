# Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости.
# Для парсинга использовать XPath. Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
# Сложить собранные данные в БД

from lxml import html
import requests
from pymongo import MongoClient
import pandas as pd
from datetime import date, timedelta

client = MongoClient('127.0.0.1', 27017) # localhost and port
db = client['HH_vacancy'] # база данных
news_db = db.vacancy # коллекция

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
response = requests.get('https://yandex.ru/news/', headers=header)
dom = html.fromstring(response.text)

data = dom.xpath("//article")

news = []
for d in data:
    new_dict = {}
    istochnik = d.xpath(".//a[@class='mg-card__source-link']/text()")
    naimenovanie_novosti = d.xpath(".//h2[@class='mg-card__title']/text()")
    naimenovanie_novosti = naimenovanie_novosti[0].replace('\xa0', ' ')
    links = d.xpath(".//h2[@class='mg-card__title']/../@href")
    data = d.xpath(".//span[@class='mg-card-source__time']/text()")
    if 'вчера' in data[0]:
        yesterday = date.today() - timedelta(days=1)
        data = data[0].split()
        time = yesterday.strftime('%Y-%m-%d') + ' '+ data[2]
        data = pd.to_datetime(time)
    else:
        data = pd.to_datetime(data[0])

    new_dict['istochnik'] = istochnik
    new_dict['naimenovanie_novosti'] = naimenovanie_novosti
    new_dict['links'] = links
    new_dict['data'] = data

    news.append(new_dict)

news_db.insert_many(news)