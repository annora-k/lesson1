import csv
import re

def get_bus_stops(filename):
    with open(filename, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f, delimiter=';')

        bus_stop_list = []
        
        for row in reader:
            bus_stop_list.append((row['Name'], row['geoData']))

    return bus_stop_list


def get_coord(coord_string):
	pass


result = get_bus_stops('busstop.csv')
print(result)

def get_coord(coord_string):
    return re.findall(r'([\d\.]+)', coord_string)

def set_coord(name, coord_string)
