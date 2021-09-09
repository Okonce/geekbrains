import requests

url = 'https://upload.wikimedia.org/wikipedia/commons/0/09/POL_2007_08_04_Jaroslawiec_zachodniopomorskie_02.JPG'

response = requests.get(url)  #.encoding('UTF-8')


if response.status_code == 200:
    pass

if response.ok:   # 200..399
    pass

response.raise_for_status()

response.text

with open('file.jpg', 'wb') as f:
    f.write(response.content)


print()