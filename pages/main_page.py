#импорт базового класса
from pages.base_s_page import BaseSPage
#импорт класса-locators
from pages.locators import MainPageLocators
#импорт модуля inspect
import inspect

class MainPage(BaseSPage):
	def __init__(self, *args, **kwargs):
	#вызываем конструктор родителя и передаём ему аргументы, переданные в данный конструктор
		super(MainPage, self).__init__(*args, **kwargs)
	
	def should_be_main_page(self):
		#управляющая функция тестом верности страницы
<<<<<<< HEAD
		self.shoul_be_portal_url()
		self.should_be_element_on_page("Main Page", "Photo image", "Should be photo image on main page", *MainPageLocators.PHOTO_IMG)

	def should_be_order_form_on_main_page(self):
		#управляющая функция тестом наличия формы заказа на странице
		self.should_be_element_on_page("Main Page", "Order form", "Should be order form on main page", *MainPageLocators.ORDER_FORM)
		self.should_be_element_on_page("Main Page", "User name input", "Should be user name in form on main page", *MainPageLocators.USERNAME_FORM)
		self.should_be_element_on_page("Main Page", "User mail input", "Should be user mail in form on main page", *MainPageLocators.USERMAIL_FORM)
		self.should_be_element_on_page("Main Page", "User files input", "Should be user files in form on main page", *MainPageLocators.USERFILES_FORM)
		self.should_be_element_on_page("Main Page", "User comment", "Should be user comment in form on main page", *MainPageLocators.USERCOMMENT_FORM)
		self.should_be_element_on_page("Main Page", "Submit form", "Should be submit button in form on main page", *MainPageLocators.SUBMIT_FORM)
=======
		self.should_be_main_url()
		self.should_be_photo_on_main_page()

	def should_be_order_form_on_main_page(self):
		#управляющая функция тестом наличия формы заказа на странице
		self.should_be_form_on_main_page()
		self.should_be_username_on_form_on_main_page()
		self.should_be_usermail_on_form_on_main_page()
		self.should_be_userfiles_on_form_on_main_page()
		self.should_be_usercomment_on_form_on_main_page()
		self.should_be_submit_on_form_on_main_page()

	def should_be_photo_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.PHOTO_IMG), "<Main Page>Photo is not presented"
		print(inspect.stack()[0][3] + ": PHOTO_IMG Ok")
		
	def should_be_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.ORDER_FORM), "<Main Page>Order form is not presented"
		print(inspect.stack()[0][3] + ": ORDER_FORM Ok")
		
	def should_be_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.ORDER_FORM), "<Main Page>Order form is not presented"
		print(inspect.stack()[0][3] + ": ORDER_FORM Ok")
		
	def should_be_username_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.USERNAME_FORM), "<Main Page>UserName on form is not presented"
		print(inspect.stack()[0][3] + ": USERNAME_FORM Ok")
		
	def should_be_usermail_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.USERMAIL_FORM), "<Main Page>UserMail on form is not presented"
		print(inspect.stack()[0][3] + ": USERMAIL_FORM Ok")
		
	def should_be_userfiles_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.USERFILES_FORM), "<Main Page>UserFiles on form is not presented"
		print(inspect.stack()[0][3] + ": USERFILES_FORM Ok")
		
	def should_be_usercomment_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.USERCOMMENT_FORM), "<Main Page>UserComment on form is not presented"
		print(inspect.stack()[0][3] + ": USERCOMMENT_FORM Ok")
		
	def should_be_submit_on_form_on_main_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*MainPageLocators.SUBMIT_FORM), "<Main Page>Submit on form is not presented"
		print(inspect.stack()[0][3] + ": SUBMIT_FORM Ok")
		
	def should_be_main_url(self):
		# проверка на корректный url адрес
		uri = "/Irina622/portfolio/"
		url = self.browser.current_url
#		print ("\nMainPage:should_be_ware_url()")
#		print ("\nself.browser.current_url ='" + url + "' (" + str(url.find(uri)) + "; url_len=" + str(len(url)) + "; len=" + str(len(uri)) + "; " + str(len(url)-url.find(uri)-len(uri)) + ")")
		assert 0 < url.find(uri), "<Main Page>URI is wrong"
		print(inspect.stack()[0][3] + ": uri Ok")
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467

#пустая строка в конце файла
