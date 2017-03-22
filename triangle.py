def get_triangle(a, b, c):
	a = int(a)
	b = int(b)
	c = int(c)

	if (a >= b+c) or (b >= a+c) or ((c >= a+b)):
		result = 4
	else:
		if a==b==c:
			result = 1
		elif a == b or b == c or c == a:
			result = 2
		else:
			result = 3
	return result

a = input('Введите число 1: ')
b = input('Введите число 2: ')
c = input('Введите число 3: ')

result1 = get_triangle(a, b, c)
print(result1)