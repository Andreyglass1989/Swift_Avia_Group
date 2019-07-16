# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import xlrd, xlwt
import re 

# интеграция с Гугл таблицами
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint, re
# интеграция с Гугл таблицами
#чтение файла с клиентами
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


# интеграция с Гугл таблицами
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/root/Рабочий стол/Avia-Logistic-503d3df31fe1.json', scope)
client = gspread.authorize(creds)
sheet_google = client.open(u'Отправка новая почта').sheet1
sheet_new = client.open(u'Отправка новая почта')
list01 = sheet_new.worksheets()
#получение последнего листа таблицы
sheet_work = sheet_new.worksheet(list01[-1].title)
# интеграция с Гугл таблицами

""" for exel """
book = xlwt.Workbook(encoding="utf-8")
sheet_no = book.add_sheet("Sheet 1")
sheet_no.write(0, 0, "Client")
sheet_no.write(0, 1, "Phone")
sheet_no.write(0, 2, "Code")
sheet_no.write(0, 3, "EDRPOU")
sheet_no.write(0, 4, "Organization")
sheet_no.write(0, 5, "Address")
""" for exel """

#нахождение не существующих клиентов в файле
list_of_lists = sheet_work.get_all_values()
listClient_noname = []
listPhoneNumber_noname = []
listClientAddress_noname = []
for row_val in list_of_lists[1:]:
	if row_val[1] not in data_client:
		listClient_noname.append(row_val[1])
		listPhoneNumber_noname.append(row_val[2])
		match = re.findall(r'[0-9-+]{9,20}', r'%s'%row_val[2])
		# print(match[0] if match else 'Not found') 
		if match:
			listClientAddress_noname.append(match[0])
		else:
			listClientAddress_noname.append("None")
dictionary = {
# "client": listClient_noname, 
			  "phone": listClientAddress_noname,
			  "address": listPhoneNumber_noname }
data_client_noname = pd.DataFrame(dictionary, index=listClient_noname)
for i in range(len(data_client_noname)):
	#сохранение их в файл
	sheet_no.write(i+1, 0, data_client_noname.index[i])
	sheet_no.write(i+1, 1, data_client_noname.iloc[i]['phone'])
	sheet_no.write(i+1, 5, data_client_noname.iloc[i]['address'])
	#сохранение их в файл	
	print(data_client_noname.iloc[i]['address'])
	print(data_client_noname.index[i])
print(data_client_noname)
book.save("/root/Yandex.Disk/самолеты/ГЖ/new-client-phone.xls")
print("Не забудьте. Скопируйте данные с файла: /самолеты/ГЖ/new-client-phone.xls в существующий!!!!") 
#нахождение не существующих клиентов в файле



#прописывает всех клиентов(кроме одесситов) из сайта в гугл таблицы 
for i in range(len(df)):
	if df.iloc[i]['client'] not in odessa:
		print(df.iloc[i]['client'])
		a=data_client[data_client['client'] == df.iloc[i]['client']]['address'].to_string()
		# print(a)
		# print(len(a))
		if len(a) != 0 or a != "":
			print(a)
	    # sheet_work.update_cell(i+2, 1, df.iloc[i]['pcs'])
	    # sheet_work.update_cell(i+2, 2, df.iloc[i]['client'])
	    # sheet_work.update_cell(i+2, 6, df.iloc[i]['weight0']+"kg")