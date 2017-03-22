with open('referat.txt', 'r', encoding = 'utf-8') as file:
	words = file.read()

	numbers = words.split()
	numbers= len(numbers)
	print('Количество слов - {}. '.format(numbers))
