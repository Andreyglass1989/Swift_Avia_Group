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
#Авторизация на Новой почте
driver.get('https://new.novaposhta.ua/#/login')
p = raw_input('Нажми Enter как прогрузиться страница ')
driver.find_element_by_css_selector('input#input_0[name="email"]').send_keys('1989andreyglass@gmail.com')
driver.find_element_by_css_selector('input#input_1[name="password"]').send_keys('qwerty12345')
driver.find_element_by_css_selector('button#login-btn-login[type="submit"]').click()
#
# Создаем накладную
p = raw_input('Нажми Enter как прогрузиться страница ')
driver.find_element_by_css_selector('button#sidebar-btn-invoice-create[type="button"]').click()



p = raw_input('Нажми Enter как выберится checkbox ')
# driver.find_element_by_id('mat-checkbox-9-input').click()

driver.find_element_by_css_selector('input#mat-input-36').send_keys('10,5')
driver.find_element_by_css_selector('input#mat-input-37').send_keys('0,05')
driver.find_element_by_css_selector('input#mat-input-38').send_keys('1')
driver.find_element_by_css_selector('input#mat-input-34').send_keys(u'Господарські та побутові товари')
driver.find_element_by_css_selector('button#edit-invoice-btn-create').click()

# p = raw_input('Нажми Enter как прогрузиться страница ')
# driver.find_element_by_css_selector('input#mat-input-30').click()

# driver.find_element_by_css_selector('input#mat-input-18').send_keys('0937190220')


p = raw_input('Выберите отправителя вручную: ')
# driver.find_element_by_css_selector('input#mat-input-16').send_keys('0952077866')
p = raw_input('Input date and press enter to continue: ')
driver.find_element_by_css_selector('button#edit-invoice-btn-save').click()