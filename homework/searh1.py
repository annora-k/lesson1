list_name = ['Вася', 'Маша', 'Петя', 'bvfdgdf', 'Саша', 'Даша']

def find_person(name):
	for names in list_name:
		if name == names:
			return names
			

def find_person2(name):
	if name in list_name:
		return name

result = find_person('Валера')
print(result)

