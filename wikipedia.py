import requests 
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Potato'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table', {'class':'wikitable'}, {'style': 'float:right; clear:left; width:18em;'})

countries = []
productionRates = []

rows = table.find_all('tr')
for row in rows:
	cells = row.find_all('td')
	if len(cells) > 1:
		country = cells[0]
		countries.append(country.text.strip())

		productionRate = cells[1]
		productionRates.append(productionRate.text.strip())
print(countries)
print(productionRates)