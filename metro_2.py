import csv
from datetime import datetime

with open('moscow_metro_info.csv', 'r', encoding='utf-8') as f:
	
	reader = csv.DictReader(f, delimiter=';')
	repair = []

	for row in reader:
			if row['Ремонт эскалаторов']:
				#print(row['Ремонт эскалаторов'])
				date_today = datetime.now()
				date = row['Ремонт эскалаторов']
				date = date.split('-')
				date_1 = datetime.strptime(date[0],'%d.%m.%Y')
				date_2 = datetime.strptime(date[1],'%d.%m.%Y')
				#if date_today >= date_1 and date_today <= date_2:
				if date_1 <= date_today <= date_2:
					repair.append(row['Станция метрополитена'])

			
print(set(repair))