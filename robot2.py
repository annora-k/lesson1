import os
import psutil
import sys
import shutil

print('Привет, я могу рассказать тебе о системе')

answer = input('Нажми Да, если хочешь поработать. Или 0, чтобы завершить работу. \n')
if answer == "да":
		print('Отлично!')
		print("""
		1 - посмотреть, что в директории\n
		2 - какие процессы запушены в системе\n
		3 - процессор\n
		4 - информация о подключенных пользователях\n
		5 - платформа ОС\n
		6 - дублирование указанного файла\n
		7 - дублирование всех файлов в директории\n
		8 - удаление файлов"""
		)
else:
		print("Я тебя не понимаю(")

choise = ''

while choise != "0":
	print("Если хотите завершить работу нажмите 0")
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
	elif choise == '6': # Дублирование указаного файла
		if os.path.isfile(file_list[i]):  #проверка на то что указанный файл, действительно файл
			old_file = input('Введите имя файла, для копирования \n')
			new_file = old_file + '.dupl'
			shutil.copy(old_file, new_file) 
			print("Файл создан, чтобы посмотреть, его в директории, выберите действие 1")
	elif choise == '7': #дублирование всех файлов в категории
		file_list = os.listdir()
		i = 0
		while i < len(file_list):
			if os.path.isfile(file_list[i]):  #проверка на файлы и директории
				newfile_list = file_list[i] + '.dupl'
				shutil.copy(file_list[i], newfile_list)
			i +=1
	elif choise == '8': #удаление дублей из директории
		print("Текущая выбраннная директория - {}".format(os.getcwd()))
		dirname  = input("Выберите директорию: ")
		file_list = os.listdir(dirname)
		i = 0
		while i < len(file_list):
			fullname = os.path.join(dirname, file_list[i]) # функция join формирует полное имя файла
			if fullname.endswith('.dupl'): #проверяет окончание файла
				os.remove(fullname)
			i +=1

	else:
		print("Нет такого действия. \n")

	