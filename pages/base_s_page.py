#импорт базового класса
from pages.base_page import BasePage
#импорт класса-locators
from pages.locators import BaseSPageLocators
<<<<<<< HEAD
import inspect
=======

print("\n\n------------------------\n")
print("НАДО!!! ДОБАВИТЬ! (file:[base_s_page.py])")
print("1) Тест ссылок из мобильное меню")
print("2) Страница Контакты")
print("3) Настраиваемость сообщений об удачном проходе теста и их нумерация")
print("\n------------------------\n")
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467

class BaseSPage(BasePage):
	def __init__(self, *args, **kwargs):
		#вызываем конструктор родителя и передаём ему аргументы, переданные в данный конструктор
		super(BaseSPage, self).__init__(*args, **kwargs)

	def should_be_base_links_on_page(self):
<<<<<<< HEAD
		self.full_page_demensions()
		#управляющая функция тестом наличия всех обязательных ссылок на странице
		self.should_be_element_on_page("Base S Page", "About link", "Should be about link in desktop menu on page", *BaseSPageLocators.ABOUT_LINK)
		self.should_be_element_on_page("Base S Page", "Main link", "Should be main link in desktop menu on page", *BaseSPageLocators.MAIN_LINK)
		self.should_be_element_on_page("Base S Page", "Portfolio link", "Should be portfolio link in desktop menu on page", *BaseSPageLocators.PORTFOLIO_LINK)
		self.should_be_element_on_page("Base S Page", "Contact link", "Should be contact link in desktop menu on page", *BaseSPageLocators.CONTACT_LINK)
		self.should_be_element_on_page("Base S Page", "Bottom-element", "Should be Bottom-element in footer menu on page", *BaseSPageLocators.BOTTOM)
		self.should_be_element_on_page("Base S Page", "Scype link", "Should be scype link in footer on page", *BaseSPageLocators.SCYPE_LINK)
		self.should_be_element_on_page("Base S Page", "Github link", "Should be github link in footer on page", *BaseSPageLocators.GITHUB_LINK)

	def shoul_be_portal_url(self):
		# проверка на корректный url адрес (портала = домена)
		url = self.browser.current_url
#		print ("\n<BaseSPage>:shoul_be_portal_url()")
#		print ("\nself.browser.current_url ='" + url + "' (" + str(url.find(uri)) + "; url_len=" + str(len(url)) + "; len=" + str(len(uri)) + "; " + str(len(url)-url.find(uri)-len(uri)) + ")")
		if (self.report_type == 0):
			assert 0 < url.find(self.portal_name), "<BaseSPage>URL portal is wrong"
			print(inspect.stack()[0][3] + ": portal name Ok")#в шапку import inspect
		else:
			if (0 < url.find(self.portal_name)):
				res = self.rep_pass
			else:
				res = self.rep_fail
			self.check_list_add(name_test="Correct domain name in URL", result_test=res, stat_test=True)
#			self.check_list_add(name_test=inspect.stack()[0][3].replace("_", " "), result_test=res)#в шапку import inspect

	def should_be_page_uri(self, uri_page, url):
		# проверка на корректный url адрес страницы
#		print ("\nself.browser.current_url ='" + url + "' (" + str(url.find(uri)) + "; url_len=" + str(len(url)) + "; len=" + str(len(uri)) + "; " + str(len(url)-url.find(uri)-len(uri)) + ")")
		if (self.report_type == 0):
			assert 0 < url.find(uri_page), "<BaseSPage Page>URI page is wrong"
			print(inspect.stack()[0][3] + ": uri_page Ok")#в шапку import inspect
		else:
			if (0 < url.find(uri_page)):
				res = self.rep_pass
			else:
				res = self.rep_fail
			self.check_list_add(name_test="Correct page name in URI", result_test=res)
#			self.check_list_add(name_test=inspect.stack()[0][3].replace("_", " "), result_test=res)#в шапку import inspect
=======
		#управляющая функция тестом наличия всех обязательных ссылок на странице
		self.should_be_about_link_on_page()
		self.should_be_main_link_on_page()
		self.should_be_portfolio_link_on_page()
		self.should_be_contact_link_on_page()
		self.should_be_scype_link_on_page()
		self.should_be_github_link_on_page()

	def should_be_about_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.ABOUT_LINK), "<Base S Page>About link is not presented"
		print("ABOUT_LINK Ok")

	def should_be_main_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.MAIN_LINK), "<Base S Page>Main link is not presented"	
		print("MAIN_LINK Ok")

	def should_be_portfolio_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.PORTFOLIO_LINK), "<Base S Page>Portfolio link is not presented"	
		print("PORTFOLIO_LINK Ok")

	def should_be_contact_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.CONTACT_LINK), "<Base S Page>Contact link is not presented"	
		print("CONTACT_LINK Ok")

	def should_be_scype_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.SCYPE_LINK), "<Base S Page>Scype link is not presented"	
		print("SCYPE_LINK Ok")

	def should_be_github_link_on_page(self):
		#тест: показан ли элемент на страничке, не показан = ошибка
		assert self.is_element_present(*BaseSPageLocators.GITHUB_LINK), "<Base S Page>Github link is not presented"	
		print("GITHUB_LINK Ok")
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467

#пустая строка в конце файла
