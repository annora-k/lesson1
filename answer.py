def get_answer(question):
	answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	return answer.get(question.lower())

print(get_answer('ПРИВЕТ'))
print(get_answer('Как ДеЛа'))
print(get_answer('поКа'))


