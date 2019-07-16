# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = True
binary = FirefoxBinary('/root/FireFox/firefox/firefox')
#driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)

driver = webdriver.Firefox(firefox_binary=binary)
#driver.get("http://inventwithpython.com")

#write and send form
#Авторизация
driver.get('https://drive.google.com/drive/my-drive')
p = raw_input('Нажми Enter как прогрузиться страница ')
driver.find_element_by_css_selector('input#identifierId[name="identifier"]').send_keys('1989andreyglass@gmail.com')
driver.find_element_by_css_selector('div#identifierNext').click()
p = raw_input('Нажми Enter как прогрузиться страница ')
# print(p)
driver.find_element_by_css_selector('input[type="password"]').send_keys('0937190220')
# [name="password"]
driver.find_element_by_css_selector('div#passwordNext').click()
p = raw_input('Нажми Enter как прогрузиться страница ')