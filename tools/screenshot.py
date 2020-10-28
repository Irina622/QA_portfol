#Функции:
#1) Создаёт главную подпаку скриншотов (переменная screenshot_folder->self.subdir)
#2) создаёт подпаку для скриншотов текущего текущего теста (на основании даты-времени).
#Создание - на стадии инициализации класса, т.е. папка будет доступна далее
#3) в переменной self.path хранится созданный путь для текущих скриншотов (self.ensure_dir())

import time#для работы счетчика времени
import os	#работа с ОС: текущий каталог
import datetime	#работа с датой-временем

class Screenshot():
	def __init__(self, screenshot_folder):
		self.subdir = screenshot_folder	#подпапка для хранения файлов-скринов
		self.path = self.name_folder()	#имя подкаталога
		self.ensure_dir(self.path + "test.file")

	def ensure_dir(self, file_path):
	#проверяем существование директории, если её нет - создаём, включая подпапки
	#file_path - полный путь вместе с именем файла
		dr = os.path.dirname(file_path)
		if not os.path.exists(dr):
			os.makedirs(dr)
	
	def name_folder(self):
	#формируем имя подкаталога, включая полный путь к нему, без имени файла
		curdir = os.path.dirname(os.path.abspath(__file__))
		prj = curdir.rsplit('/', maxsplit=2)[1]
#		print("Screenshot::name_folder() prj=<"+prj+">")
		now = datetime.datetime.now()
		date_time = now.strftime("%Y_%m_%d_%H_%M_%S")
		file_name = date_time
#		print("Screenshot::name_folder() peturn=<"+"./" + prj + "/" + self.subdir + "/" + file_name + "/"+">")
		return "./" + prj + "/" + self.subdir + "/" + file_name + "/"
	
#пустая строка в конце файла
