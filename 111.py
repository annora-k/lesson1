def get_answer(question):
	
	#question = str.lower(question)
	question = str(question).lower()
	
	dialog  = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

	return dialog.get(question)

a = get_answer('КаК ДеЛА')

print(a)