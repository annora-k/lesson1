from flask import Flask
from names import get_names

app = Flask(__name__)

@app.route("/")
def index():
	return 'Перейдите на страницу /names, чтобы увидеть имена'


@app.route("/names")
def print_names():
	data = get_names("https://apidata.mos.ru/v1/datasets/2009/rows")
	result = '''
	<html>
		<head></head>
		<body>
			<table border=1>
				<tr>
					<th>Имя</th>
					<th>Год</th>
					<th>Месяц</th>
					<th>Количество</th>
				</tr>
		'''
	if data:
		for name in data:
			result += '<tr>'
			result += '<td>{}</td>'.format(name['Cells']['Name'])
			result += '<td>{}</td>'.format(name['Cells']['Year'])
			result += '<td>{}</td>'.format(name['Cells']['Month'])
			result += '<td>{}</td>'.format(name['Cells']['NumberOfPersons'])
			result += '</tr>\n'

	result += '''
			</table>
		</body>
	</html>
	'''

	
	return result




@app.route("/names/<int:years_born>")
def year_born(years_born):
	data = get_names("https://apidata.mos.ru/v1/datasets/2009/rows")
	years_id = [name for name in data if name['Cells']['Year'] == years_born]
	#if years_born in name['Cells']['Year']
	
	result = '''
	<html>
		<head></head>
		<body>
			<table border=1>
				<tr>
					<th>Имя</th>
					<th>Год</th>
					<th>Месяц</th>
					<th>Количество</th>
				</tr>
		'''
	if years_id:
		for name in years_id:
			result += '<tr>'
			result += '<td>{}</td>'.format(name['Cells']['Name'])
			result += '<td>{}</td>'.format(name['Cells']['Year'])
			result += '<td>{}</td>'.format(name['Cells']['Month'])
			result += '<td>{}</td>'.format(name['Cells']['NumberOfPersons'])
			result += '</tr>\n'

	result += '''
			</table>
		</body>
	</html>
	'''
	


	return 'Дети одного года %s' % result

	




if __name__ == '__main__':
	app.run()