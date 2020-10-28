import time#для работы счетчика времени
import os	#работа с ОС: текущий каталог
import datetime	#работа с датой-временем
import xlsxwriter	#работа с excel-файлами (*.xlsx)
import pandas as pd	#работа с модулем pandas
#Установлен пакет Pandas для работы с экселем, т.к. текущий пакет {xlsxwriter} не позволяет ЧИТАТЬ из ячейки того экселя который сейчас же сам и пишет и уже открыл...

class Report():
	def __init__(self, type_report):
		self.type_report = type_report#тип отчета: 0 - assert/отладка, 1 - check_list to *.xlsx, также смотри test_page.py::report
		self.subdir = "rep/"#подпапка для хранения файлов-отчетов
		self.ext_xlsx = ".xlsx"#разрешение экселевского файла
		self.report = []#массив=чек-лист [index] => [page_name;browser resolution;name_test;result_test;stat_test], также смотри base_page.py
		self.file_name = self.name_file()#имя файла без расширения

	def to_xlsx(self):
	#работа с экселем: создаём файл, переносим в него отчет
		print("File-report: <" + self.file_name + self.ext_xlsx + ">")
		if (len(self.report) > 0):
			self.ensure_dir(self.file_name + self.ext_xlsx)
			wb = xlsxwriter.Workbook(self.file_name + self.ext_xlsx)
			left = wb.add_format({'align': 'left'})
			center = wb.add_format({'align': 'center'})
			generals = []	#вспомогательный; приходится городить такое т.к. модуль xlsxwriter не умеет читать из Экселя, даже из того который сам сейчас же и пишет; [index] = {self.report.key; k1}, т.е. взаимосвязь названия теста (которые self.report.stat=1) и индекса строки в экселе, куда он был записан
			df = pd.DataFrame()	#вспомогательный; приходится городить такое т.к. модуль xlsxwriter не умеет читать из Экселя, даже из того который сам сейчас же и пишет; таблица=двумерный массив, копирующий эксель при чем <passed> и <failed> в эксель здесь равны 1, оставщиеся пустыми ячейки - предполагаются для заполнения <skipped>. Строка dataFrama = Строка Excel. Столбец dataFrama = Столбец+1 Excel
			wsh2 = wb.add_worksheet('Check-List')
			wsh2.set_column('A:A', 45)
			wsh2.set_column('B:B', 25)
			k = 1	#первая рабочая строка - номер строки в экселе
			#BEGIN внешние условия
			wsh2.write('A'+str(k), 'Browser', left)
			wsh2.write('A'+str(k+1), 'Browser resolution', left)
			wsh2.write('A'+str(k+2), 'Page name', left)
			#END внешние условия
			k1 = k #номер текущего теста (номер текущей итерации в чек-листе) номер строки с названием теста в эксель
			l = 1 #номер текущей итерации внешних условий в чек-листе (номер колонки в эксель)
			for br_name,resol,page,key,val,stat in self.report:
				if k1 == 1:
					cur_br = br_name
					cur_resol = resol
					cur_page = page
					wsh2.write(k-1, l, br_name, center)
					wsh2.write(k, l, resol, center)
					wsh2.write(k+1, l, page, center)
					wsh2.write('A'+str(k1+3), key, left)
					wsh2.write(k1+2, l, val, center)
					generals.append([key, k1+3])
					df.at[k1+3, l] = 1
				else:
					if (br_name != cur_br)or(cur_resol != resol)or(cur_page != page):
						l = l + 1
						wsh2.set_column(l, l, 25)
						cur_br = br_name
						cur_resol = resol
						cur_page = page
						wsh2.write(k-1, l, br_name, center)
						wsh2.write(k, l, resol, center)
						wsh2.write(k+1, l, page, center)
						df.at[k1+3, l] = 1
					if stat == False:
						wsh2.write('A'+str(k1+3), key, left)
						wsh2.write(k1+2, l, val, center)
						df.at[k1+3, l] = 1
					else:
						gen = self.generals_getIndex(generals=generals, findKey=key)
						if gen == 0:
						#такой ключ еще (на текущей итерации) НЕ попадался в self.report
							wsh2.write('A'+str(k1+3), key, left)
							wsh2.write(k1+2, l, val, center)
							generals.append([key, k1+3])
							df.at[k1+3, l] = 1
						else:
						#такой ключ уже (на текущей итерации) попадался в self.report
							wsh2.write(gen-1, l, val, center)
							df.at[gen, l] = 1
							k1 = k1 - 1
				k1 = k1 + 1
#			print(df)
			#второй проход по экселю - расставляем <Skipped> на основании анализа заполненности массива skips
			#indx (при переборе) = l (при введении данных) = колонка. Внимание! колонка "В" имеет индекс "1"
			#col - столбец с данными в экселе/dataFrame
			#i = номер строки в экселе / индекс для col
			for indx, col in df.iteritems():
				for i in col.index:
					if col[i] != 1:
#						print("["+str(indx)+"]["+str(i)+"] => ["+str(col[i])+"] ->> 'Skipped'")
						wsh2.write(i-1, indx, "Skipped", center)
			wb.close()
	
	def generals_getIndex(self, generals=[], findKey=""):
	#проверяем существование в массиве generals элемента с ключем (именем теста) findKey
		res = 0
		for key,index in generals:
			if key == findKey:
				return index
		return res
	
	def ensure_dir(self, file_path):
	#проверяем существование директории, если её нет - создаём
	#file_path - полный путь вместе с именем файла
		dr = os.path.dirname(file_path)
#		print("ensure_dir() <"+dr+">")
		if not os.path.exists(dr):
			os.makedirs(dr)
	
	def name_file(self):
	#формируем имя файла, включая полный путь к нему, но без расширения
		curdir = os.path.dirname(os.path.abspath(__file__))
		prj = curdir.rsplit('/', maxsplit=1)[1]
		now = datetime.datetime.now()
		date_time = now.strftime("%Y_%m_%d_%H_%M_%S")
		file_name = prj + "_" + date_time
		return "./" + prj + "/" + self.subdir + file_name
	
	def to_console(self):
	#выводим отчет в консоль
		for br_name,resol,page,key,val,stat in self.report:
			print(str(br_name),"[",str(resol),"] ","<",str(page),"> '",str(key),"' => '",str(val),"' [",str(stat),"]")
	
	def add(self, rep=[]):
	#добавляем к существующему отчету данные в виде массива в нужном формате
		self.report += rep

#пустая строка в конце файла
