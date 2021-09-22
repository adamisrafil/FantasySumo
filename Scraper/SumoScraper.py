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
              'wrestler1Result': row.find_all('td', class_='tk_kekka')[0].find('img').get('src'),
              'Rikishi1': row.find('td', class_='tk_east').find('center').text,
              'Technique': row.find('td', class_='tk_kim').text,
              'Rikishi2': row.find('td', class_='tk_west').find('center').text,
              'wrestler2Result': row.find_all('td', class_='tk_kekka')[1].find('img').get('src'),
            }
	for row in topDivTable]

	for row in cleaned_rows:
		if row['wrestler1Result'] == 'img/hoshi_kuro.gif':
			row['wrestler1Result'] = "Loser"
			row['wrestler2Result'] = "Winner"
		elif row['wrestler2Result'] == 'img/hoshi_kuro.gif':
			row['wrestler2Result'] = "Winner"
			row['wrestler1Result'] = "Loser"
	
	pprint(cleaned_rows)

if __name__ == '__main__':
	for day in range(1,16):
		scrapeDayOfSumo(day)