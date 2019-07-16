from LK.models import (
    Pack, 
    PackProduct,
    PackStatus,
    ParcelPackProduct, 
    Currency,
    CategoryGroup,
    Language,
    PartnerInc2Sandbox,
)
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
import xlrd, xlwt
from decimal import Decimal
import pandas as pd


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

# для чтения файлов англ --- русский
listEng = []
listChina = []
rb = xlrd.open_workbook(u'/root/django/swift_avia_group/advanced/Alexander partner/eng_rus_partner_Alexander.xlsx',formatting_info=False)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
  row = sheet.row_values(rownum)
  listEng.append(row[0])
  listChina.append(row[1])
data = pd.Series(listChina, index=listEng)
listNewEng = []
listNewRus = []
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
sheet1.write(0, 0, "Русский")
sheet1.write(0, 1, "Английский")
i=0
# для чтения файлов англ --- русский



wb = xlrd.open_workbook(u'/root/django/swift_avia_group/advanced/Alexander partner/28+od.xlsx')
# type(wb) получаем список всех листов текущего документа
sheet_names = wb.sheet_names()

for name_sheet_item in sheet_names:
	xl_sheet = wb.sheet_by_name(name_sheet_item)
	print(xl_sheet.name)
	last_partner = PartnerInc2Sandbox.objects.all().last()
	last_partner = int(last_partner.number)+1
	PartnerInc2Sandbox.objects.create(number=str(last_partner))

	pack_partner = Pack(
		pack_number = str(last_partner),
		customer_id = 1005,
		pack_status = PackStatus.objects.get(pack_status_id=1), 
		volume = 1,
		weight = 1,
		point = 1,
		comment = xl_sheet.name,
		external_id = "",
		total= 1,
		currency_code = "USD",
		currency_value= 1.0,
		sandbox= 0,
		def_field = 0,
		packlist = 0,
		sklad_id = 6,
		# sklad = Sklad.objects.get(sklad_id=1),
		language = Language.objects.get(language_id=2),
		currency = Currency.objects.get(currency_id=2),
		category_group = CategoryGroup.objects.get(category_group_id = 3))
	pack_partner.save()

	# https://blogs.harvard.edu/rprasad/2014/06/16/reading-excel-with-python-xlrd/
	xl_sheet = wb.sheet_by_name(xl_sheet.name)
	xl_sheet.nrows #к-во строк

	for rownum in range(1, xl_sheet.nrows):
	  name = xl_sheet.cell_value(rownum, 9)
	  # print(name in data)
	  # если перевод существуею считать его с файл если нет перевести гугл транслейтом и сохранить в новый файл
	  if name in data:
	  	print(name, data[name])
	  	name_en = data[name]
	  else:
	  	print("TRANSLATE")
		#google translate
		translation = translate_client.translate(
			name,
			target_language=target)
		name_en = translation['translatedText']
		i = i+1
		sheet1.write(i, 0, name)
		sheet1.write(i, 1, name_en)
		#google translate

	  quantity_xls = xl_sheet.cell_value(rownum, 12)
	  print(name, quantity_xls)
	  quantity_xls = Decimal(quantity_xls)
	  price_xls = xl_sheet.cell_value(rownum, 20)
	  price_xls = Decimal(price_xls)
	#Проставление веса продуктов если значение не пусто
	  if  xl_sheet.cell_value(rownum, 17) != u'' or xl_sheet.cell_value(rownum, 17) is not u'':
	  	weight_xls = xl_sheet.cell_value(rownum, 17)
	  	weight_xls = Decimal(weight_xls)
	  else:
	  	weight_xls = 0.00001
	  	weight_xls = Decimal(weight_xls)
	  
	  url_link = xl_sheet.cell_value(rownum, 24)

	  PackProduct(pack = pack_partner, name = name_en, price = price_xls, quantity = quantity_xls, item_class_id = 0, 
	  		weight = weight_xls, weight_netto = 0.00, volume = 0.5, point = 1, url = url_link).save()

book.save("/root/django/swift_avia_group/advanced/Alexander partner/new_eng_rus.xls")
print("Не забудь скопировать новые названия в старый файл")