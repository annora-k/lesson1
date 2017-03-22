import csv

answers = {
	"привет": "И тебе привет!",
	"как дела": "Лучше всех", 
	"пока": "Увидимся"
}

# with open('answer.csv', 'w', encoding='utf-8') as f:
# 	fields = ['привет', 'как дела', 'пока']
# 	writer = csv.DictWriter(f, fields, delimiter=';')
# 	writer.writeheader()
# 	writer.writerow(answers)

with open('answer.csv', 'w', encoding='utf-8') as f:
	
	writer = csv.writer(f, delimiter=';')
	for key, value in answers.items():
		writer.writerow([key, value])
