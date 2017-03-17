def get_text(text1, text2):
	a = None

	if text1 == text2:
		a  = 1
	elif len(text1) > len(text2):
		a = 2
	elif  text2 == 'learn':
		a = 3

	return a

print('Привет')

text1 = input('Введите строку 1: ')
text2 = input('Введите строку 2: ')

result = get_text(text1, text2)
print(result)
