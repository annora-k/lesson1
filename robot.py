import os
import psutil
import sys

print('Привет, я могу рассказать тебе о системе')

answer = ''

while answer != "0":

	answer = input('Нажми Да, если хочешь поработать. Или 0, чтобы завершить работу. \n')

	if answer == "да":
		#print('Отлично!')
		print("""
		1 - посмотреть, что в директории\n
		2 - какие процессы запушены в системе\n
		3 - процессор\n
		4 - информация о подключенных пользователях\n
		5- платформа ОС\n"""
		)
		
		choise = input("Укажите номер действия: \n")

		if choise == '1':
			print("Это то что находится в директории \n {}".format(os.listdir()))
		elif choise == '2':
			print("Это процессы: \n {}".format(psutil.pids()))
		elif choise == '3':
			print("Это процессор: \n {}".format(psutil.cpu_times(percpu=True)))
		elif choise == '4':
			print("Информация о пользователях: \n {}".format(psutil.users()))
		elif choise == '5':
			print("Версия ОС: \n {}".format(sys.platform))
		else:
			print("Нет такого действия. \n")
	else:
		print("Я тебя не понимаю(")