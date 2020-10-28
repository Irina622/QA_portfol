<<<<<<< HEAD
#для работы pytest: параметризация, маркеры
import pytest
#для работы счетчика времени
import time

#импорт класса Report
from report import Report
#импорт класса Screenshot
from tools.screenshot import Screenshot

=======
#для работы параметризации
import pytest
#для работы счетчика времени
import time
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467
#импорт класса главной страницы MainPage
from pages.main_page import MainPage
#импорт класса страницы AboutPage
from pages.about_page import AboutPage
#импорт класса страницы ContactPage
from pages.contact_page import ContactPage

<<<<<<< HEAD
#тип отчета о тесте:
#0 - assert
#1 - check_list to *.xlsx
report = 1

#подпапка для скриншотов
#подпапка первого уровня, в проессе создаются подпапки внутри этой папки = для каждого теста свой
#формат "screens" - без слэшей начального-конечного
screenshot_folder = "screens"


@pytest.fixture(scope="class")
def scr_shoots(request):
	version = "1.0 формируем общий каталог скриншотов"
	scr = Screenshot(screenshot_folder)
		
	def teardown():
		print("\nteardown scr()")
	request.addfinalizer(teardown)
		
	return scr


@pytest.fixture(scope="class")
def ch_list(request):
	version = "3.0 работаем с классом-отчетом"
	rep = Report(report)
		
	def teardown():
		if (rep.type_report == 0):
#			print("Type report = consol")
			rep.to_console()
		else:
#			print("Type report = xlsx")
			rep.to_xlsx()
	request.addfinalizer(teardown)
		
	return rep

			
class Test_portal():
	@pytest.mark.main_page
	def test_guest_main_page(self, browser, ch_list, scr_shoots):
		#тестируем страницу <main_page>
		link = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/Irina622/portfolio/master/index.html"
		page = MainPage(browser=browser, url=link, report_type=report, \
			portal_name="/Irina622/portfolio/", page_name="Main", \
			screenshot_folder=scr_shoots.path)
		page.clear_cookies()#чистим куки
		page.open()#открываем в браузере link
		time.sleep(2)
		page.should_be_main_page()#общие тесты для страницы
		page.should_be_base_links_on_page()
		page.should_be_order_form_on_main_page()
		ch_list.add(page.check_list)#добавляем результаты тестирования страницы в общий отчет
		if page.test_result == False:
			page.screening()#если необходимо - делаем скриншот
		assert True

	@pytest.mark.about_page
	def test_guest_about_page(self, browser, ch_list, scr_shoots):
		#тестируем страницу <about_page>
		link = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/Irina622/portfolio/master/about.html"
		page = AboutPage(browser=browser, url=link, report_type=report, \
			portal_name="/Irina622/portfolio/", page_name="About", \
			screenshot_folder=scr_shoots.path)
		page.clear_cookies()#чистим куки
		page.open()#открываем в браузере link
		time.sleep(2)
		page.should_be_about_page()#общие тесты для страницы
		page.should_be_base_links_on_page()
		ch_list.add(page.check_list)#добавляем результаты тестирования страницы в общий отчет
		if page.test_result == False:
			page.screening()#если необходимо - делаем скриншот
		assert True

	@pytest.mark.contact_page
	def test_guest_contact_page(self, browser, ch_list, scr_shoots):
		#тестируем страницу <contact_page>
		link = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/Irina622/portfolio/master/contact.html"
		page = ContactPage(browser=browser, url=link, report_type=report, \
			portal_name="/Irina622/portfolio/", page_name="Contact", \
			screenshot_folder=scr_shoots.path)
		page.clear_cookies()#чистим куки
		page.open()#открываем в браузере link
		time.sleep(2)
		page.should_be_contact_page()#общие тесты для страницы
		page.should_be_base_links_on_page()
		page.should_be_order_form_on_contact_page()
		ch_list.add(page.check_list)#добавляем результаты тестирования страницы в общий отчет
		if page.test_result == False:
			page.screening()#если необходимо - делаем скриншот
		assert True
=======
@pytest.mark.main_page
class TestMainPage():
	def test_guest_main_page(self, browser):
		link = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/Irina622/portfolio/master/index.html"
		page = MainPage(browser=browser, url=link)
		page.open()
		page.should_be_main_page()
		page.should_be_base_links_on_page()
		page.should_be_order_form_on_main_page()
		time.sleep(2)

@pytest.mark.about_page
class TestAboutPage():
	def test_guest_about_page(self, browser):
		link = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/Irina622/portfolio/master/about.html"
		page = AboutPage(browser=browser, url=link)
		page.open()
		page.should_be_about_page()
		page.should_be_base_links_on_page()
		time.sleep(2)

@pytest.mark.contact_page
class TestContactPage():
	def test_guest_contact_page(self, browser):
		link = "https://htmlpreview.github.io/?https://raw.githubusercontent.com/Irina622/portfolio/master/contact.html"
		page = ContactPage(browser=browser, url=link)
		page.open()
		page.should_be_contact_page()
		page.should_be_base_links_on_page()
		page.should_be_order_form_on_contact_page()
		time.sleep(2)
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467

#пустая строка в конце файла
