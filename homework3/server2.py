from flask import Flask, abort, request
from names import get_names

app = Flask(__name__)

@app.route("/")
def index():
	return 'Перейдите на страницу /names, чтобы увидеть имена'


@app.route("/names")
def print_names():
	year = int(request.args.get('year'))

	data = get_names("https://apidata.mos.ru/v1/datasets/2009/rows")

	years_born = [name for name in data if name['Cells']['Year'] == year]

	result = '''
	<table>
		<tr>
			<th>Имя</th>
			<th>Год</th>
			<th>Месяц</th>
			<th>Количество</th>
		</tr>
	'''
	
	for name in years_born:
		result += '<tr>'
		result += '<td>{}</td>'.format(name['Cells']['Name'])
		result += '<td>{}</td>'.format(name['Cells']['Year'])
		result += '<td>{}</td>'.format(name['Cells']['Month'])
		result += '<td>{}</td>'.format(name['Cells']['NumberOfPersons'])
		result += '</tr>\n'

	result += '''
			</table>
	'''

	
	return result



if __name__ == '__main__':
	app.run(port=5001, debug=True)
