1. Create Django app "Izrael"
2. Create models "IzraelDataForPacking"
3. Register into Admin and Settings
------------------------------------------------

4. Append Data file in BaseData

""" Read Data in File """

# -*- coding: utf-8 -*-
import xlrd, xlwt

from Izrael.models import IzraelDataForPacking

rb = xlrd.open_workbook('/root/Yandex.Disk/самолеты/israel/18.01.19/xx2682UA.xlsx',formatting_info=False)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
  row = sheet.row_values(rownum)
  if row[9] != "#Н/Д" and row[6] !='': 
  	post_code = int(row[6]) 
  else: 
  	post_code = unicode(row[6])
  b2 = IzraelDataForPacking(box_number=int(row[0]), full_customer_name=row[2], telephone_number=row[3], oblast=row[4],
                city=row[5], post_number=post_code, street_home=row[7], height=row[14], description=row[15] )
  b2.save()

<!--   print(row[0])
  print(row[2])
  print(row[3])
  print(row[4])
  print(row[5])
  if row[6] != "#Н/Д" and row[6] !='':
  	print(int(row[6]))
  else:
  	print(unicode(row[6]))
  print(row[7])
  print(row[14])
  print(row[15])
  print("----") -->


  ------------------------------------------------------------------------

Проблемы:
1. Кирилицу отображает черными квадратиками
  - поставить шрифты попробовать

2. Может сползать текст на страницах
  - сделать отдельно table для Notify address