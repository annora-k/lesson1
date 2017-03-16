from answer import get_answer

def ask_user():
	while True:
		try:
			question = input('Введите вопрос: ')

			print(get_answer(question))

			if question.lower() == 'пока':
				break

		except KeyboardInterrupt:
			print('\nНельзя так выйти, напиши "пока"')

ask_user()
