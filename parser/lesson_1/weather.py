import requests

url = 'https://api.openweathermap.org/data/2.5/weather'
city = 'Arkhangelsk'
appid = 'e5e4cd692a72b0b66ea0a6b80255d1c3'

params = {'q': city,
          'appid': appid}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

response = requests.get(url, params=params, headers=headers)

j_data = response.json()

print(f"В городе {j_data['name']} температура {j_data['main']['temp'] - 273.15} градусов")