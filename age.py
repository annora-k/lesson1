print('Привет')

age =  input('Введете свой возраст: ')
age = round(float(age))

if age < 7:
	print('Ты ходишь в детский сад')

elif age >=7 and age < 18:
	print('Ты учишься в школе')

elif age >= 18 and age < 23:
	print('Вы учитесь в ВУЗе')

elif age >= 23:
	print('Вы работаете')

