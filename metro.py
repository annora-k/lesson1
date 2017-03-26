import csv

with open('moscow_metro_info.csv', 'r', encoding='utf-8') as f:
	
	reader = csv.DictReader(f, delimiter=';')
	
	repair = []
	for row in reader:
		if row['Ремонт эскалаторов']:
			repair.append(row['Станция метрополитена'])

print(set(repair))