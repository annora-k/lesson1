list_name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

while list_name:
	if list_name.pop(0) == 'Валера':
		print('Валера нашелся')
		break

print(list_name)
