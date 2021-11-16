from bs4 import BeautifulSoup
from pprint import pprint
import requests

def scrapeDayOfSumo(day):
    print(f'Day: {day}')
    html = requests.get(f'http://sumodb.sumogames.de/Results.aspx?b=202109&d={day}')
    soup = BeautifulSoup(html.text, "html.parser")

    tables = soup.find("table", {"class":"tk_table"})
    topDivTable = tables.find_all('tr')
    topDivTable.pop(0)
    cleaned_rows = [
            {
                'wrestlerResult': row.find_all('td', class_='tk_kekka')[0].find('img').get('src'),
                'RikishiE': row.find('td', class_='tk_east').find('center').text,
                'Technique': row.find('td', class_='tk_kim').text,
                'RikishiW': row.find('td', class_='tk_west').find('center').text,
            }
    for row in topDivTable]

    for row in cleaned_rows
        if row['wrestlerResult'] == 'img/hoshi_kuro.gif' or 'img/hoshi_fusensho.gif'
            row['wrestlerResult'] = "East"
        else
            row['wrestlerResult'] = "West"

    print(cleaned_rows)

if __name__ == '__main__':
    for day in range(1,15):
        scrapeDayOfSumo(day)

# with open('OutputDump.txt','w') as dump:

