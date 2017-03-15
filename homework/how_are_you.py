def ask_user():
	while True:
		answer = input('Как дела? ')

		if answer.lower() == 'хорошо':
			break

ask_user()
