question= input('Как дела? ')

def get_ask(question):
	a  = 'Как дела? '
	return a

while True:
	if question == 'Хорошо':
		print('Пока')
		break
	else:
		ask = get_ask(question)
		print(ask)
		break
	


def find_person(name):
