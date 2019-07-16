# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import xlrd, xlwt
from LK.models import Air

# интеграция с Гугл таблицами
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint, re
# интеграция с Гугл таблицами


capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = True
binary = FirefoxBinary('/root/FireFox/firefox/firefox')
driver = webdriver.Firefox(firefox_binary=binary)

listClient = []
listPhoneNumber = []
listClientAddress = []
rb = xlrd.open_workbook('/root/Yandex.Disk/самолеты/ГЖ/Клиент-телефон-НП.xlsx',formatting_info=False)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
  row = sheet.row_values(rownum)
  listClient.append(row[0])
  listPhoneNumber.append(row[1])
  listClientAddress.append(row[5])
  # listClientAddress
dictionary = {
			  "client": listClient, 
			  "phone": listPhoneNumber,
			  "address": listClientAddress }
data_client = pd.DataFrame(dictionary)

#список одесситов
odessa = ["20/000028", "23/000013", 
"25/001180", "27/001271",  "35/000193", "35/000218", "36/000135", "41/000314", "75/000698", "22/000464", 
"62/000105", "57/000040", "75/000590", "27/000460", "62/000130", "333/000012", "30/002210", "23/000888",
"16/000907", "61/001192", "22/000674", "33/005021", "07/010679", "14/000031", "89/000008", "62/000365", 
"12/000044", "98/000513", "93/000681", "98/000519"]
none_odessa = list(data_client["client"])


#Авторизация
a = raw_input("Введите какой самолет A...? - ")
air = Air.objects.get(name=a)

url = "http://aviapostdelivery.com/admin/index.php?route=sale/parcel_ua/printair&token=05b293d2cfd707d91ad4bc676f90304c&air_id={0}".format(air.air_id)
driver.get(url)
# p = raw_input('Нажми Enter как прогрузиться страница login-aviapostdelivery ')
driver.find_element_by_css_selector('input#input-username[name="username"]').send_keys('aUkraine')
driver.find_element_by_css_selector('input#input-password[name="password"]').send_keys('fw94kqmd020JJddeW')
driver.find_element_by_css_selector('button[type="submit"]').click()

#Чтения данных с таблицы
# table = driver.find_elements_by_tag_name('table')
body = driver.find_element_by_tag_name('tbody')
file_data = []
df = pd.DataFrame(columns=['client', 'weight0', 'volume0', 'weight1', 'volume1', 'raz_weight', 'raz_volume', 'pcs'])
body_rows = body.find_elements_by_tag_name('tr')
for row in body_rows:
    data = row.find_elements_by_tag_name('td')
    file_row = []
    for datum in data:
        datum_text = datum.text.encode('utf8')
        file_row.append(datum_text)
    
    file_data.append(file_row)
df = pd.DataFrame(file_data, columns=['client', 'weight0', 'volume0', 'weight1', 'volume1', 'raz_weight', 'raz_volume', 'pcs'])
print(df)

#Гугл таблицами
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/root/Рабочий стол/Avia-Logistic-503d3df31fe1.json', scope)
client = gspread.authorize(creds)
sheet = client.open(u'Отправка новая почта').sheet1
sheet_new = client.open(u'Отправка новая почта')
list01 = sheet_new.worksheets()
#получение последнего листа таблицы
sheet_work = sheet_new.worksheet(list01[-1].title)

#Авторизация на НОВОЙ ПОЧТЕ
driver.get('https://new.novaposhta.ua/#/login')
p = raw_input('Нажми Enter как прогрузиться страница Авторизации новой почты ')
driver.find_element_by_css_selector('input#input_0[name="email"]').send_keys('1989andreyglass@gmail.com')
driver.find_element_by_css_selector('input#input_1[name="password"]').send_keys('qwerty12345')
driver.find_element_by_css_selector('button#login-btn-login[type="submit"]').click()
# # Создаем накладную
p = raw_input('Нажми Enter как загрузится личный кабинет ')
driver.find_element_by_css_selector('button#sidebar-btn-invoice-create[type="button"]').click()
otvet='y'
df_save=[]
# Выбор клиента
data_client.set_index("client", inplace=True)





while otvet != 'n':
	a = raw_input('Введите код клиента и нажмите Enter ')
	d=df[df['client']==a]
	volume_0 = float(d.iloc[0]['volume0'])/167
	print(d.iloc[0]['client'], d.iloc[0]['weight0'], volume_0, d.iloc[0]['pcs'])
	# выбор клиента
	# p = raw_input('Нажми Enter как выберится checkbox ')
	driver.find_element_by_css_selector('input[placeholder="Загальна вага"]').send_keys(d.iloc[0]['weight0'])
	driver.find_element_by_css_selector('input[placeholder="Загальний об’єм"]').send_keys(str(volume_0))
	driver.find_element_by_css_selector('input[placeholder="Кількість місць"]').clear()
	driver.find_element_by_css_selector('input[placeholder="Кількість місць"]').send_keys(d.iloc[0]['pcs'])
	driver.find_element_by_css_selector('input[placeholder="Опис відправлення"]').send_keys(u'Господарські та побутові товари')
	driver.find_element_by_css_selector('textarea[placeholder="Додаткова інформація про відправлення (не обов’язково)"]').send_keys(d.iloc[0]['client'])
	driver.find_element_by_css_selector('button#edit-invoice-btn-create').click()
	#гугл таблица чтение значений адрессов с таблицы
	address = sheet_work.col_values(2)

	if a in data_client.index:
		driver.find_element_by_css_selector('input[placeholder="Пошук у контактах (шукайте за ПІБ, телефоном, назвою компанії)"]').send_keys(data_client.loc[a]['phone'])
		# driver.find_element_by_css_selector('input[placeholder="Пошук у контактах (шукайте за ПІБ, телефоном, назвою компанії)"]').send_keys(data_client[a])

	elif a not in data_client.index:
		phone = raw_input('Введите номер телефона ')
		driver.find_element_by_css_selector('input[placeholder="Пошук у контактах (шукайте за ПІБ, телефоном, назвою компанії)"]').send_keys(phone)
		d1 = pd.Series(phone, index=[a])
		# df_save = df_save.append(d1)


	driver.find_element_by_css_selector('input[placeholder="Контакт"]').click()
	# print(phone)
	raw_input('проверьте внимательно ПРАВИЛЬНОСТЬ! ')
#Создаем накладную
	driver.find_element_by_css_selector('button#edit-invoice-btn-save').click()
	#Сохранение трэк-номера в google таблицы
	# Получаю трэк-номер
	treck=driver.find_element_by_class_name("invoice-header__number")
	treck.text
	#
	""" Возникает ошибка если такого номера нет в списке отправок на нп """
	if a in address: #or sheet_work.col_values(2)
		# amount_re = re.compile(r'%s' %data_client[a])
		cell = sheet_work.find(a) #amount_re
		new_col = cell.col+3
		sheet_work.update_cell(cell.row, new_col, treck.text)

	# elif a not in address:
		# amount_re = re.compile(r'%s' %df_save[-1])
		# cell = sheet_work.find(amount_re)
		# new_col = cell.col+3
		# sheet_work.update_cell(cell.row, new_col, treck.text)
	"""  """


	otvet = raw_input('Желаете продолжить? y/n ')
	driver.find_element_by_css_selector('button#edit-invoice-btn-next-template').click()
else:
	print(df_save)
	driver.find_element_by_css_selector('button#edit-invoice-btn-ready').click()



# book.save("/root/Yandex.Disk/самолеты/ГЖ/new-client-phone.xls")
