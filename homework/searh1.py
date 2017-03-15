list_name = ['Вася', 'Маша', 'Петя', 'bvfdgdf', 'Саша', 'Даша']

def find_person(name):
	for names in list_name:
		if name == names:
			return names
			
result = find_person('Валера')
print(result)


