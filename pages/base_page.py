#Основные функции не привязанные к конкретному сайту
<<<<<<< HEAD
#Константы (заданы как переменные, не предполагается их изменение):
#1) self.rep_pass и self.rep_fail - задают соответственно ключевые слова
# для обозначения результатов теста.
#2) self.screenshot_ext - расширение файла-скриншота
#3) self.screen_height_addition - дополнительный размер для определения размера страницы сайта

#Переменные класса:
#1) self.browser - экземпляр объекта Браузер (см. conftest.py)
#2) self.url - задаёт текущий URI тестируемой страницы
#3) self.check_list - текущий отчет о тестировании [массив]
#4) self.report_type - задаёт формат отчета о тетировании: 
# <0> - командная строка (реализация через assert) Не рекомендую, т.к. ошибки приводят
# к останову всего тестирования, <1> - xlsx-файл  (см. report.py)
#5) self.portal_name - доменное имя портала (общее для всех тестируемых страниц)
#6) self.page_name - имя тестируемой страницы (в чек-лист пойдёт)
#7) self.screenshot_folder - путь к каталогу для сохранения скриншотов (см. ./tools/screenshot.py)
#8) self.page_full_height, self.page_full_width - текущие размеры страницы,
# включая невидимые области на экране
#9) self.test_result - обобщенный результат тестов на странице: если хоть 1 неудачный - false

#Вспомогательные функции (не предполгается использование в других классах-файлах):
#1) self.is_element_present() - проверяет существование элемента (return True)
# на текущей странице соглавно селектора. Отстствие элемента не вызывает прекращение
# работы.
#2) self.is_not_element_present() - поиск элемента на странице в течение 
# определённого времени. Элемента не должно быть по-дефаулту, но потом должен проявиться. 
# Return - требуется разобраться (практика, stepik).
#3) self.is_disappeared() - поиск элемента на странице в течение 
# определённого времени. Элемент должен быть по-дефаулту, но потом должен исчезнуть.
# Return - требуется разобраться (практика, stepik).
#4) self.check_list_add() - добавляем в массив чек-листа (self.check_list)
# новую запись с результатами теста.
#5) self.full_page_demensions() - определяем максимальные размеры страницы. 
#Инициируем переменные self.page_full_height, self.page_full_width. Неявный
#вызов из класса BaseSPage

#Глобальные функции (для запуска извне класса-файла):
#1) self.is_element() - поиск элемента на странице. Запуск ТОЛЬКО после 
# def is_element_present()=true, т.к. ошибки приведут к прекращению всего теста.
# Return - ссылку на искомый элемент.
#2) self.open() - открывает в окне браузера страницу с указанным адресом (url, self.url).
#3) self.clear_cookies() - чистим браузер от ранее сохранённых куков.
#4) self.should_be_element_on_page() - реализация простого теста на наличие
# элемента на странице. Т.е. надстройка над def is_element_present().
# Автоматически ведётся лог в зависимости от self.report_type
# В случае ошибок автоматически создаются скрины.
#5) self.screening() - создаём скриншот текущего состояния браузера и сохраняем его

import os	#работа с ОС: текущий каталог
import datetime	#работа с датой-временем
import time	#работа со временем-паузы в процессе
=======
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467
#импорт исключения NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
#импорт исключения TimeoutException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
<<<<<<< HEAD
#импорт класса-locators
from pages.locators import BaseSPageLocators

class BasePage():
	def __init__(self, browser, url, portal_name, page_name, screenshot_folder, \
		report_type=0):
	#инициируем переменные класса:
		#BEGIN VARS
		self.browser = browser	#текущий браузер из conftest.py
		self.url = url	#ссылка для перехода по методу self.open()
		#чек-лист в виде массива: [index] => [page_name;browser resolution;name_test;result_test;stat_test], где result_test из ряда: passed, skipped, failed; stat_test only True/False
		self.check_list = []	#отчет о текущей странице
		self.report_type = report_type	#тип отчета о тесте: 0 - assert; 1 - check_list
		self.portal_name = portal_name	#доменное имя портала
		self.page_name = page_name	#имя страницы (в чек-лист пойдёт)
		self.screenshot_folder = screenshot_folder #подпапка для хранения скринов
		self.page_full_height = 0
		self.page_full_width = 0#текущие размеры страницы, включая невидимые области
		self.test_result = True #обобщенный результат тестов на странице: если хоть 1 неудачный - будет false
		#END VARS
		#BEGIN CONSTS
		self.rep_pass = "Passed"	#тест удачен
		self.rep_fail = "Failed"	#тест не удачен
		self.screenshot_ext = ".png"	#расширение файла-скриншота
		self.screen_height_addition = 25	#дополнительный размер для определения размера страницы сайта
		#END CONSTS
		#BEGIN предварительные вычисления
		#END предварительные вычисления
=======

class BasePage():
	def __init__(self, browser, url, timeout=10):
	#инициируем класс
		self.browser = browser
		self.url = url
#		self.browser.implicitly_wait(timeout)
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467
	
	def is_element_present(self, how, what):
	#поиск элемента на странице: если есть - return true, else false
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True
	
	def is_not_element_present(self, how, what, timeout=20):
	#поиск элемента на странице в течение времени: если есть - ?return true, else false?
	#элемента не должно быть по-дефаулту, но потом должен проявиться
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False
	
	def is_disappeared(self, how, what, timeout=20):
	#поиск элемента на странице в течение времени: если есть - ?return true, else false?
	#элемент должен быть по-дефаулту, но потом должен исчезнуть
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).\
				until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
		return True
	
	def is_element(self, how, what):
	#поиск элемента на странице: запуск после def is_element_present()=true
		return self.browser.find_element(how, what)
	
	def open(self):
	#открываем ссылку
		self.browser.get(self.url)
<<<<<<< HEAD
		
	def should_be_element_on_page(self, modul_name, test_elem_name, caption, how, what):
	#реализация простого теста на наличие элемента на странице: true - всё гут
	#т.е. надстройка над def is_element_present(self, how, what)
	#Автоматически ведётся лог в зависимости от self.report_type
	#В случае ошибок автоматически создаются скрины
	#modul_name - вспомогательная: имя модуля вызвавшего проверку для скорейшего поиска багов, виден только к режиме report_type = 0, также влияет на автоматическую установку stat_test в режиме report_type = 1
	#test_elem_name - вспомогательная: название тестируемого элемената для скорейшего поиска багов, виден только к режиме report_type = 0
	#caption - название теста для передачи в чек-лист
	#page_name - название страницы, вызвавшей тест - для формирования чек-листа
	#how, what - пара локаторов из файла locators.py (всегда должны быть последними в списке переменных при вызове функции)
		if (self.report_type == 0):
			assert self.is_element_present(how, what), "<"+modul_name+">"+test_elem_name+" is not presented"	
			print(test_elem_name+" Ok")
		else:
			if (self.is_element_present(how, what) == True):
				res = self.rep_pass
			else:
				res = self.rep_fail
				self.test_result = False
			#по имени модуля определяем - общая проверка, или индивидуальная
			if modul_name == "Base S Page":
				stat_test = True
			else:
				stat_test = False
			self.check_list_add(name_test=caption, result_test=res, stat_test=stat_test)
	
	def check_list_add(self, name_test, result_test, stat_test=False):
	#добавляем в массив чек-листа (self.check_list) новую запись
	#stat_test = True = общая проверка, False - индивидуальная/уникальная проверка
		#все свойства self.browser.capabilities
		#cap = self.browser.capabilities
		#for key,val in cap.items():
		#	print(key, "=>", val)
		resolution = self.browser.get_window_size()
		if 'browserVersion' in self.browser.capabilities:
			br_ver = self.browser.capabilities['browserVersion']
		else:
			br_ver = self.browser.capabilities['version']
		self.check_list.append([self.browser.name + " " + br_ver, "{}x{}".format(resolution["width"], resolution["height"]), self.page_name, name_test, result_test, stat_test])

	def clear_cookies(self):
	#чистим браузер от куков
		self.browser.delete_all_cookies()

	def full_page_demensions(self):
	#определяем максимальные размеры страницы. Неявный вызов из класса BaseSPage
	#Тестировалась правильность работы только для явной прокрутки страницы
	#Неявную необходимо смотреть отдельно
		el_bot = self.is_element(*BaseSPageLocators.BOTTOM)
		self.page_full_height = el_bot.location["y"] + el_bot.size["height"] + self.screen_height_addition
		el_body = self.is_element(*BaseSPageLocators.BODY)
		self.page_full_width = el_body.size["width"]
#		print("BasePage::full_page_on_screen() [" + str(el_bot.location["y"]) + "; " + str(el_bot.size["height"]) + "; " + str(self.screen_height_addition) + "]")

	def screening(self, caption=""):
	#создаём скриншот текущего состояния браузера и сохраняем его в self.screenshot_folder
		if (len(caption) > 1):
			caption = "-" + caption
#		print("BasePage::screening("+self.page_name+caption+") = ["+self.screenshot_folder+"]")
		resolution = self.browser.get_window_size()#сохраняем текущее разрешение экрана
		self.browser.set_window_size(self.page_full_width, self.page_full_height+1000)
		time.sleep(2)
		self.browser.save_screenshot(self.screenshot_folder+self.page_name+caption+self.screenshot_ext)
		self.browser.set_window_size(resolution["width"], resolution["height"])
		time.sleep(2)
=======

>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467

#пустая строка в конце файла
