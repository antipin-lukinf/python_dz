import requests
from bs4 import BeautifulSoup



def pogod():
    pog = 'https://world-weather.ru/pogoda/russia/yemva/'

    r = requests.get(pog)
    soup = BeautifulSoup(r.text, 'html.parser')

    for temp in soup.find_all('div', id = 'weather-now-number'):
        temp = temp.text

    for obl in soup.find_all('span', id_ = 'weather-now-icon'):
        obl = obl.get('title')

    for dr in soup.find_all('div', id='weather-now-description'):

        line = dr.text
        last_index = 0
        itog = []
        for i, char in enumerate(line[1:-9]):
            if char.istitle() or i == len(line[1:-10]):
                itog.append(line[last_index:i + 1])
                last_index = i + 1
        itog.append(line[-10:-4])
        itog.append(line[-4:])
        dr = ' '.join(itog[:-5])

    send_tg = f'Погода в Емве ' + '\n' + temp + ' ' + obl + '\n' + dr + '\n'
    print(send_tg)