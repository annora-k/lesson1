list_scores = [{'class':'4 класс', 'scores':[4, 3, 5, 2, 3]},
			   {'class':'5 класс', 'scores':[5, 5, 4, 2, 4]}, 
			   {'class': '6 класс', 'scores':[2, 2, 3, 5, 5]}]

school_score_sum = 0
school_score_number = 0

for classes in list_scores:
	print('Класс: {}'.format(classes['class']))
	class_score = sum(classes['scores'])
	class_score_number = len(classes['scores']) 

	print('Средняя оценка по классу: {}'.format(class_score / class_score_number))

	school_score_sum += class_score
	school_score_number += class_score_number


print('Средняя оценка по школе {}'.format(school_score_sum / school_score_number))