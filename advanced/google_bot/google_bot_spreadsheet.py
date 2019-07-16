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
print(data_client)


#список одесситов
odessa = ["20/000028", "23/000013", 
"25/001180", "27/001271",  "35/000193", "35/000218", "36/000135", "41/000314", "75/000698", "22/000464", 
"62/000105", "57/000040", "75/000590", "27/000460", "62/000130", "333/000012", "30/002210", "23/000888", 
"61/001192", "16/000907", "22/000674", "33/005021", "07/010679", "14/000031", "89/000008", "62/000365", 
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
# sheet_work = sheet_new.worksheet(list01[-2].title)

#создание нового листа и прописание первых строк
sheet_work = sheet_new.add_worksheet(title=a.decode('utf-8'), rows="150", cols="10")
sheet_work = sheet_new.worksheet(a.decode('utf-8'))

sheet_work.update_acell('A1', u'мест')
sheet_work.update_acell('B1', u'клиент')
sheet_work.update_acell('C1', u'адресс')
sheet_work.update_acell('D1', u'коммент')
sheet_work.update_acell('E1', u'трэк-номер')
sheet_work.update_acell('F1', u'Вес')

# интеграция с Гугл таблицами

#прописывает всех клиентов(кроме одесситов) из сайта в гугл таблицы 
pd.options.display.max_colwidth = 100
for i in range(len(df)):
	if df.iloc[i]['client'] not in odessa:
		# print(i, df.iloc[i]['client'])
		sheet_work.update_cell(i+2, 1, df.iloc[i]['pcs'])
		sheet_work.update_cell(i+2, 2, df.iloc[i]['client'])
		sheet_work.update_cell(i+2, 6, df.iloc[i]['weight0']+"kg")
		#если есть адрес в файле прописать его в 3 колонку гугл таблицы
		if df.iloc[i]['client'] in none_odessa:
			a=data_client[data_client['client'] == df.iloc[i]['client']]['address'].to_string(index=False)
			if len(a) != 0 or a != "":
				sheet_work.update_cell(i+2, 3, a)