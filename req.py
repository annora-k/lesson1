import requests

def get_weather(url):
	result = requests.get(url)
	print(type(result.json))
	
	if result.status_code == 200:
		return result.json()
		#print(result.json()['sys']['country'])
		#print(result.json()['main'])
	else:
		print("Что то не то")

if __name__ == "__main__":
	get_weather("http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID=20ae3a94ba29866cbd1999d35f5644d4&units=metric")