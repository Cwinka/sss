from requests import get
from bs4 import BeautifulSoup
from pandas import DataFrame
print('Подключаюсь к яндекс погоде ...')
try:
    page = get('https://yandex.ru/pogoda/iset?via=reg')
except Exception:
    print('Интернет включи, дурик с:')
    input()
soup = BeautifulSoup(page.content, 'html.parser')
print('Получаю информацию ...')
city = soup.find_all('span', class_='breadcrumbs__title')[-1].text

names = soup.find_all('div', class_='forecast-briefly__name')[4:10]
temp_days = soup.find_all('div', class_='temp forecast-briefly__temp forecast-briefly__temp_day')[4:10]
temp_nights = soup.find_all('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night')[4:10]
conditions = soup.find_all('div', class_='forecast-briefly__condition')[4:10]

week_list = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

name_list = [one_name.text for one_name in names]
name_list[0] = f'{name_list[0]} ({week_list[week_list.index(name_list[1]) - 1]})'
name_list[1] = f'Завтра ({name_list[1]})'
day_list = [one_temp_day.text[4:] for one_temp_day in temp_days]
night_list = [one_temp_night.text[5:] for one_temp_night in temp_nights]
condition_list = [one_condition.text for one_condition in conditions]
print('Делаю красивую табличку ...')
weather = DataFrame(
    {   str(city): '',
        'День недели': name_list,
        'Днем': day_list,
        'Ночью': night_list,
        'Краткое описание': condition_list
    })
print(weather)
ss = input()
