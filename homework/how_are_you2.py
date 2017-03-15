def get_answer(question):
	answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	return answer.get(question.lower(), 'Не понял вопроса')


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
