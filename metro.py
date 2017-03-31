import csv
from datetime import datetime

with open('moscow_metro_info.csv', 'r', encoding='utf-8') as f:
	
	reader = csv.DictReader(f, delimiter=';')
	
	repair = []
	for row in reader:
		if row['Ремонт эскалаторов']:
			repair.append(row['Станция метрополитена'])

			date_today = datetime.now()
			date = row['Ремонт эскалаторов']split('-')
			date_1 = date[0]
			date_2 = date[1]

			if row['Ремонт эскалаторов']



print(set(repair))