import json
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('127.0.0.1', 27017) # localhost and port
db = client['HH_vacancy'] # база данных
vacancy = db.vacancy # коллекция

with open('/Users/assimarakhimbekova/PycharmProjects/geekbrains/parser/lesson_2/vacancy_list.json', 'r') as f:
    vacancy_list = json.load(f)

vacancy_list_dicts = []
for x in range(len(vacancy_list['Наименование вакансии'])):
    inner_dict = {}
    inner_dict['Наименование вакансии'] = vacancy_list['Наименование вакансии'][f'{x}']
    inner_dict['Ссылка на вакансию'] = vacancy_list['Ссылка на вакансию'][f'{x}']
    inner_dict['Минимальная з/п'] = vacancy_list['Минимальная з/п'][f'{x}']
    inner_dict['Максимальная з/п'] = vacancy_list['Максимальная з/п'][f'{x}']
    inner_dict['Валюта'] = vacancy_list['Валюта'][f'{x}']
    vacancy_list_dicts.append(inner_dict)

# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию,
# записывающую собранные вакансии (из ДЗ2) в созданную БД.
def all_vacancy(data):
    vacancy.insert_many(data)

# 2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы.
def zp(zp_value):
    for item in vacancy.find({'Минимальная з/п': {'$gt': zp_value}}): # lte меньше или равно gte - больше или равно
        pprint(item)

# 3. Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта

def new_add(new_vacancy):
    try:
        vacancy.insert_one(new_vacancy)  # так лучше делать чем many
    except:
        ...