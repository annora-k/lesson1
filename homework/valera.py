list_name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_person(name):
	while list_name:
		if list_name.pop(0) == name:
			print('{} нашелся'.format(name))
			break

print(list_name)

name = input('Введиет имя: ')
find_person(name)
