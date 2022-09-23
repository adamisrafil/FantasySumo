from bs4 import BeautifulSoup
from pprint import pprint
import requests
import csv

def scrapeDayOfSumo(day):
	print(f'Day: {day}')
	html = requests.get(f'http://sumodb.sumogames.de/Results.aspx?b=202209&d={day}')
	soup = BeautifulSoup(html.text, "html.parser")

	tables = soup.find("table", {"class":"tk_table"})
	topDivTable = tables.find_all('tr')
	topDivTable.pop(0)
	fieldnames = ['wrestler1Result', 'Rikishi1', 'Technique', 'Rikishi2', 'wrestler2Result']
	bouts = [
            {
              'wrestler1Result': row.find_all('td', class_='tk_kekka')[0].find('img').get('src'),
              'Rikishi1': row.find('td', class_='tk_east').find('center').find('a').text,
              'Technique': row.find('td', class_='tk_kim').contents[1].text,
              'Rikishi2': row.find('td', class_='tk_west').find('center').find('a').text,
              'wrestler2Result': row.find_all('td', class_='tk_kekka')[1].find('img').get('src'),
            }
	for row in topDivTable]

	for bout in bouts:
		if bout['wrestler1Result'] == 'img/hoshi_kuro.gif':
			bout['wrestler1Result'] = "Loser"
			bout['wrestler2Result'] = "Winner"
		elif bout['wrestler2Result'] == 'img/hoshi_kuro.gif':
			bout['wrestler2Result'] = "Winner"
			bout['wrestler1Result'] = "Loser"
	
	pprint(bouts)

	writeCSV(day, bouts)
	# updateRikishi(rikishiName, record)


def writeCSV(day, bouts):
	fieldnames = ['wrestler1Result', 'Rikishi1', 'Technique', 'Rikishi2', 'wrestler2Result']

	with open(f'bashoDay{day}.csv', 'w', encoding='UTF-8', newline='') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(bouts)

def updateRikishi(rikishi, record):
	fieldnames = ['wrestler1Result', 'Rikishi1', 'Technique', 'Rikishi2', 'wrestler2Result']

	with open(f'bashoDay{day}.csv', 'w', encoding='UTF-8', newline='') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(bouts)

if __name__ == '__main__':
	#which tournament
	#which days?
	for day in range(1,12):
		scrapeDayOfSumo(day)