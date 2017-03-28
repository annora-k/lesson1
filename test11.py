from flask import Flask
from req import get_weather
from datetime import datetime

city_id = 524901
apikey ='20ae3a94ba29866cbd1999d35f5644d4'

app = Flask(__name__)

@app.route("/")
def index():
	url = "http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric" % (city_id, apikey)
	weather = get_weather(url)
	cur_data = datetime.now().strftime('%d-%m-%Y')
	
	result = '<p><b>Температура:</b> %s </p>' % weather['main']['temp']
	result += '<p><b>Город:</b> %s </p>' % weather['name']
	result += '<p><b>Дата:</b> %s </p>' % cur_data
	return result

if __name__ == "__main__":
	app.run()