#импорт базового класса
from pages.base_s_page import BaseSPage
#импорт класса-locators
from pages.locators import ContactPageLocators
#импорт модуля inspect
import inspect

class ContactPage(BaseSPage):
	def __init__(self, *args, **kwargs):
	#вызываем конструктор родителя и передаём ему аргументы, переданные в данный конструктор
		super(ContactPage, self).__init__(*args, **kwargs)
	
	def should_be_contact_page(self):
		#управляющая функция тестом верности страницы
<<<<<<< HEAD
		self.shoul_be_portal_url()
		self.should_be_page_uri(uri_page="contact.html", url=self.browser.current_url)
		self.should_be_element_on_page("Contact Page", "Order button", "Should be order button in footer on contact page", *ContactPageLocators.ORDER_BOTTOM_INPUT)
		
	def should_be_order_form_on_contact_page(self):
		#управляющая функция тестом наличия формы заказа на странице
		self.should_be_element_on_page("Contact Page", "Mail form", "Should be mail form on contact page", *ContactPageLocators.MAIL_FORM)
		self.should_be_element_on_page("Contact Page", "User name", "Should be user name input in form on contact page", *ContactPageLocators.USERNAME_FORM)
		self.should_be_element_on_page("Contact Page", "User mail", "Should be user mail input in form on contact page", *ContactPageLocators.USERMAIL_FORM)
		self.should_be_element_on_page("Contact Page", "Subject", "Should be subject input in form on contact page", *ContactPageLocators.SUBJECT_FORM)
		self.should_be_element_on_page("Contact Page", "Content", "Should be content textarea in form on contact page", *ContactPageLocators.CONTENT_FORM)
		self.should_be_element_on_page("Contact Page", "Submit button", "Should be submit button in form on contact page", *ContactPageLocators.SUBMIT_FORM)
=======
		self.should_be_about_url()
		self.should_be_btn_order_bottom_on_contact_page()
		
	def should_be_order_form_on_contact_page(self):
		#управляющая функция тестом наличия формы заказа на странице
		self.should_be_form_on_contact_page()
		self.should_be_username_on_form_on_contact_page()
		self.should_be_usermail_on_form_on_contact_page()
		self.should_be_subject_on_form_on_contact_page()
		self.should_be_content_on_form_on_contact_page()
		self.should_be_submit_on_form_on_contact_page()

	def should_be_form_on_contact_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*ContactPageLocators.MAIL_FORM), "<Contact Page>Mail form is not presented"
		print(inspect.stack()[0][3] + ": MAIL_FORM Ok")

	def should_be_username_on_form_on_contact_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*ContactPageLocators.USERNAME_FORM), "<Contact Page>Name on form is not presented"
		print(inspect.stack()[0][3] + ": USERNAME_FORM Ok")

	def should_be_usermail_on_form_on_contact_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*ContactPageLocators.USERMAIL_FORM), "<Contact Page>Mail on form is not presented"
		print(inspect.stack()[0][3] + ": USERMAIL_FORM Ok")

	def should_be_subject_on_form_on_contact_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*ContactPageLocators.SUBJECT_FORM), "<Contact Page>Subject on form is not presented"
		print(inspect.stack()[0][3] + ": SUBJECT_FORM Ok")

	def should_be_content_on_form_on_contact_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*ContactPageLocators.CONTENT_FORM), "<Contact Page>Content on form is not presented"
		print(inspect.stack()[0][3] + ": CONTENT_FORM Ok")

	def should_be_submit_on_form_on_contact_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*ContactPageLocators.SUBMIT_FORM), "<Contact Page>Submit on form is not presented"
		print(inspect.stack()[0][3] + ": SUBMIT_FORM Ok")
		
	def should_be_about_url(self):
		# проверка на корректный url адрес
		uri = "/Irina622/portfolio/"
		uri_page = "contact.html"
		url = self.browser.current_url
#		print ("\nMainPage:should_be_ware_url()")
#		print ("\nself.browser.current_url ='" + url + "' (" + str(url.find(uri)) + "; url_len=" + str(len(url)) + "; len=" + str(len(uri)) + "; " + str(len(url)-url.find(uri)-len(uri)) + ")")
		assert 0 < url.find(uri), "<Contact Page>URI is wrong"
		print(inspect.stack()[0][3] + ": uri Ok")
		assert 0 < url.find(uri_page), "<Contact Page>URI is wrong"
		print(inspect.stack()[0][3] + ": uri_page Ok")

	def should_be_btn_order_bottom_on_contact_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*ContactPageLocators.ORDER_BOTTOM_INPUT), "<Contact Page>Order input (bottom) is not presented"
		print(inspect.stack()[0][3] + ": ORDER_BOTTOM_INPUT Ok")
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467

#пустая строка в конце файла
