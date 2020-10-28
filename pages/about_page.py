#импорт базового класса
from pages.base_s_page import BaseSPage
#импорт класса-locators
from pages.locators import AboutPageLocators
#импорт модуля inspect
import inspect

class AboutPage(BaseSPage):
	def __init__(self, *args, **kwargs):
	#вызываем конструктор родителя и передаём ему аргументы, переданные в данный конструктор
		super(AboutPage, self).__init__(*args, **kwargs)
	
	def should_be_about_page(self):
		#управляющая функция тестом верности страницы
<<<<<<< HEAD
		self.shoul_be_portal_url()
		self.should_be_page_uri(uri_page="about.html", url=self.browser.current_url)
		self.should_be_element_on_page("About Page", "Order button", "Should be order button on about page", *AboutPageLocators.ORDER_INPUT)
		self.should_be_element_on_page("About Page", "About link", "Should be order button in footer on about page", *AboutPageLocators.ORDER_BOTTOM_INPUT)
=======
		self.should_be_about_url()
		self.should_be_btn_order_on_about_page()
		self.should_be_btn_order_bottom_on_about_page()

	def should_be_about_url(self):
		# проверка на корректный url адрес
		uri = "/Irina622/portfolio/"
		uri_page = "about.html"
		url = self.browser.current_url
#		print ("\nMainPage:should_be_ware_url()")
#		print ("\nself.browser.current_url ='" + url + "' (" + str(url.find(uri)) + "; url_len=" + str(len(url)) + "; len=" + str(len(uri)) + "; " + str(len(url)-url.find(uri)-len(uri)) + ")")
		assert 0 < url.find(uri), "<About Page>URI is wrong"
		print(inspect.stack()[0][3] + ": uri Ok")
		assert 0 < url.find(uri_page), "<About Page>URI is wrong"
		print(inspect.stack()[0][3] + ": uri_page Ok")

	def should_be_btn_order_on_about_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*AboutPageLocators.ORDER_INPUT), "<About Page>Order input is not presented"
		print(inspect.stack()[0][3] + ": ORDER_INPUT Ok")
		
	def should_be_btn_order_bottom_on_about_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*AboutPageLocators.ORDER_BOTTOM_INPUT), "<About Page>Order input (bottom) is not presented"
		print(inspect.stack()[0][3] + ": ORDER_BOTTOM_INPUT Ok")
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467

#пустая строка в конце файла
