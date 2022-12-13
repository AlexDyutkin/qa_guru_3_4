def print_func_name(name_func, *args):
    # def - объявление функции, print_func_name - название функции в питоне, () - аргументы функции
    #  *args -

    fullname = name_func.__name__.title().replace('_', ' ') # Имя функции можно получить с помощью func.__name__
  # Метод title() возвращает строку с заглавной первой буквой каждого слова в верхний регистр.
  # replace('_', ' ') - заменяем старое значение '_' на новое ' '

    print(fullname, *args) # Напечатать Название функции, Значение аргументов

def open_browser(browser_name): #
    print_func_name(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    print_func_name(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    print_func_name(find_registration_button_on_login_page, page_url, button_text)

open_browser('Chrome')
go_to_companyname_homepage('https://qa.guru/')
find_registration_button_on_login_page('https://qa.guru/', 'login')

