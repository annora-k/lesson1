print('Привет')

text1 = input('Введите строку 1: ')
text2 = input('Введите строку 2: ')

def get_text(text1, text2):

	if text1 == text2:
		a  = 1

	else:
		a = None

	if text1 != text2:
		if len(text1) > len(text2) and text2 != 'learn':
			a = 2


		if  text2 == 'learn':
			a = 3

	#	else:
	#		a = None

	return a

result = get_text(text1, text2)
print(result)