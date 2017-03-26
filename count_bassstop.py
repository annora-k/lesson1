import csv

with open('busstop.csv', 'r', encoding='utf-8') as f:
	
	reader = csv.DictReader(f, delimiter=';')
	street = []
	for row in reader:
		street.append(row['Street'])
		#print(row['Street'])

def count_bus_stops(streets):
	bus_stops = {}
	for street in streets:
		if bus_stops.get(street):
			bus_stops[street] +=1
		else:
			bus_stops[street] = 1

	#for key, value in bus_stops.items():
		#print(key, value)

	print(sorted(bus_stops.items(), key=lambda x: x[1], reverse=True)[0])

count_bus_stops(street)
