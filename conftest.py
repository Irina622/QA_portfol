import pytest
<<<<<<< HEAD
#import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print("\n\n------------------------\n")
print("НАДО!!! ДОРАБОТАТЬ! (file:[conftest.py])")
print("1) Тесты:")
print("- ссылок из мобильное меню")
print("- определение мобильное или desktop-меню")
print("2) Автоматический чек-лист:")
print("- интегрировать условное форматирование в эксель, если поддерживает libreOffice")
print("- автоматическое определение повторяющихся вопросов, а не как сейчас тупо по переменной")
print("3) Скриншоты:")
print("- высота определяется как-то невнятно")
print("- автоматическое сравнение скриншотов ошибок с эталонным и формирование на разнице - gif")
print("4) Разрешение:")
print("- автоматическое изменение разрешений браузера")
print("\n------------------------\n")

=======
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467
def pytest_addoption(parser):
	#добавляем свои параметры в строку запуска pytest
	#--language - accept_languages браузера 
	parser.addoption('--language', \
			action='store', \
			default="en", \
			help="Choose language: ru, en, .. (etc.)")
	#--browser - имя браузера: chrome/ch; firefox/ff
	parser.addoption('--browser', \
			action='store', \
			default="chrome", \
			help="Choose browser: chrome(ch) or firefox(ff)")

def pytest_configure(config):
	#добавляем свои маркеры pytest
	config.addinivalue_line(
		"markers", "main_page: test main page at site"
	)
	config.addinivalue_line(
		"markers", "about_page: test about page at site"
	)
	config.addinivalue_line(
		"markers", "contact_page: test contact page at site"
	)
#	config.addinivalue_line(
#		"markers", "basket: test?"
#	)
	
<<<<<<< HEAD
@pytest.fixture(scope="function", autouse=True)
def get_markers(request):
#можно работать с маркерами введёнными в командую строку, результат - массив (даже из 1 элемента)
	return [marker.name for marker in request.function.pytestmark]

#@pytest.fixture(scope="function")#для каждого теста - новый запуск
@pytest.fixture(scope="module")#1 сессия = запускается 1 раз на все тесты файле
#@pytest.fixture(scope="class")#1 сессия = запускается 1 раз на все тесты классе
def browser(request):
	user_language = request.config.getoption("language")
	browser_name = request.config.getoption("browser")
=======

@pytest.fixture(scope="function")
def browser(request):
	user_language = request.config.getoption("language")
	browser_name = request.config.getoption("browser")
	
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467

	#run browser with emply sheet
	if (browser_name == "chrome")or(browser_name == "ch"):
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
<<<<<<< HEAD
		options.add_argument('--ignore-certificate-errors')
=======
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467
		print ("\n\nstart Chrome-browser for test..")
		browser = webdriver.Chrome(options=options)
	elif (browser_name == "firefox")or(browser_name == "ff"):
		fp = webdriver.FirefoxProfile()
		fp.set_preference("intl.accept_languages", user_language)
		print ("\n\nstart Firefox-browser for test..")
		browser = webdriver.Firefox(firefox_profile=fp)
	else:
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
<<<<<<< HEAD
		options.add_argument('--ignore-certificate-errors')
=======
>>>>>>> 0633da3b3b08943924294e84e95fd31f4c7aa467
		print ("\n\nYour chouse browser not supplied\nstart Chrome-browser for test..")
		browser = webdriver.Chrome(options=options)
	browser.implicitly_wait(4)

	yield browser

	print("\nquit browser..")
	browser.quit()

#пустая строка в конце файла
