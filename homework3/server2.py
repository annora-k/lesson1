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
			born_year = name['Cells']['Year']
			if born_year == 2017:
				result += '<tr>'
				result += '<td>{}</td>'.format(name['Cells']['Name'])
				result += '<td>{}</td>'.format(name['Cells']['Year'])
				result += '<td>{}</td>'.format(name['Cells']['Month'])
				result += '<td>{}</td>'.format(name['Cells']['NumberOfPersons'])
				result += '</tr>\n'
			#else:
			#	return 'Нет детей 2017 года'

	result += '''
			</table>
		</body>
	</html>
	'''


	return result

if __name__ == '__main__':
	app.run(port=5001, debug=True)
