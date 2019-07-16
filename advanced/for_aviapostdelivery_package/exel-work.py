# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import xlrd, xlwt
from decimal import Decimal

"""
Для гугл переводов
"""
# Imports the Google Cloud client library
from google.cloud import translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/root/Рабочий стол/Avia-Logistic-503d3df31fe1.json"
# Instantiates a client
translate_client = translate.Client()
target = 'en'
"""
Для гугл переводов
"""



wb = xlrd.open_workbook('/root/django/swift_avia_group/advanced/Partner/stikers.xls')
# type(wb) получаем список всех листов текущего документа
sheet_names = wb.sheet_names()
# https://blogs.harvard.edu/rprasad/2014/06/16/reading-excel-with-python-xlrd/
xl_sheet = wb.sheet_by_name(sheet_names[0])
# xl_sheet = xl_workbook.sheet_by_index(0)
xl_sheet.nrows #к-во строк
for rownum in range(1, xl_sheet.nrows):
  # row = xl_sheet.row_values(rownum)
  # print(row)
  name = xl_sheet.cell_value(rownum, 9)

#google translate
  # translation = translate_client.translate(
  #   name,
  #   target_language=target)
  # name_en = translation['translatedText']
#google translate

  quantity_xls = xl_sheet.cell_value(rownum, 12)
  quantity_xls = Decimal(quantity_xls)
  # print(type(quantity_xls))
  price_xls = xl_sheet.cell_value(rownum, 19)
  price_xls = Decimal(price_xls)
  # print(type(price_xls))
  # print(name, quantity, price)

#Проставление веса продуктов если значение не пусто
  if  xl_sheet.cell_value(rownum, 17) != u'' or xl_sheet.cell_value(rownum, 17) is not u'':
  	# print("True", rownum, xl_sheet.cell_value(rownum, 17))
  	weight_xls = xl_sheet.cell_value(rownum, 17)
  	weight_xls = Decimal(weight_xls)
  else:
  	weight_xls = 0.00001
  	weight_xls = Decimal(weight_xls)
  print(type(weight_xls))

  url_link = xl_sheet.cell_value(rownum, 24)