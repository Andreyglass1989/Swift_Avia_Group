# -*- coding: utf-8 -*-
from LK.models import (
	ParcelPackProduct,
	Parcel,
	PackProduct,
   PlombaDimension,
    )
import xlrd, xlwt
from django.core.exceptions import ObjectDoesNotExist

#read file china-english
import pandas as pd
listEng = []
listChina = []
rb = xlrd.open_workbook('/root/Yandex.Disk/самолеты/ГЖ/названия англ - китайск1 - копия (1).xlsx',formatting_info=False)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
  row = sheet.row_values(rownum)
  listEng.append(row[0])
  listChina.append(row[1])
data = pd.Series(listChina, index=listEng)
listNewEng = []
listNewRus = []
book1 = xlwt.Workbook(encoding="utf-8")
sheet2 = book1.add_sheet("Sheet 2")
sheet2.write(0, 0, "Русский")
sheet2.write(0, 1, "Английский")
#end read file china-english


# Imports the Google Cloud client library
from google.cloud import translate
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/root/Рабочий стол/Avia-Logistic-503d3df31fe1.json"

# Instantiates a client
translate_client = translate.Client()
# The target language
target = 'zh-CN'


book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 1, "item.No.")
sheet1.write(0, 2, "Poduct name (EN)")
sheet1.write(0, 3, "Poduct name (CN)")
sheet1.write(0, 4, "QTY/PCS")
sheet1.write(0, 5, "G.W/KG")
sheet1.write(0, 6, "N.W/KG")

sheet1.write(0, 7, "CTN")
sheet1.write(0, 8, "w")
sheet1.write(0, 9, "l")
sheet1.write(0, 10, "h")

sheet1.write(0, 11, "Volume")
sheet1.write(0, 12, "PCS-USD")
sheet1.write(0, 13, "Total/USD")

sheet1.write(0, 15, "QTY/PCS(_MY_EXAMPLE_)")

parcel = Parcel.objects.filter(sklad_id=1, parcel_status_id=2, date_added__contains='2019') 
# date_added__contains='2018'
i=0

z=0

for p in parcel:
   parcel_pack_product = ParcelPackProduct.objects.filter(parcel_id=p.parcel_id)
   for a in parcel_pack_product:
      i = i+1
      # print(p.external_id)
      pl = PlombaDimension.objects.get(plomba_id=p.external_id)
      vol = (pl.plomba_width/100)*(pl.plomba_height/100)*(pl.plomba_length/100)

      sheet1.write(i, 1, p.external_id)
      try:
        sheet1.write(i, 2, a.pack_product.name)

        if a.pack_product.name in data:
          sheet1.write(i, 3, data[a.pack_product.name])
        elif a.pack_product.name not in data:
          print("Translate")
          print(a.pack_product.name)
          text = a.pack_product.name
                  # Translates some text into Russian
          translation = translate_client.translate(text, target_language=target)
          sheet1.write(i, 3, translation['translatedText'])
          # i = i+1
          sheet2.write(i, 0, text)
          sheet2.write(i, 1, translation['translatedText'])

        # if a.pack_product.name in data:
        #    z = z+1
        #    sheet1.write(i, 3, data[a.pack_product.name])

        # else: 
        # #data[a.pack_product.name]
        #   sheet1.write(i, 3, '')
      except ObjectDoesNotExist:
        pass
      sheet1.write(i, 4, a.quantity)
      sheet1.write(i, 5, pl.plomba_weight)
      sheet1.write(i, 6, '')
      sheet1.write(i, 7, '1')
      sheet1.write(i, 8, pl.plomba_width)
      sheet1.write(i, 9, pl.plomba_height)
      sheet1.write(i, 10, pl.plomba_length)
      sheet1.write(i, 11, vol)

      try:
        sheet1.write(i, 12, a.pack_product.price)
      except ObjectDoesNotExist:
        pass
      sheet1.write(i, 13, '=$E2*$M2')
      sheet1.write(i, 15, '=СУММПРОИЗВ(($B$2:$B$482=$B2)*($C$2:$C$482=$C2)*($M$2:$M$482=$M2);$E$2:$E$482)')

book1.save("/root/Yandex.Disk/самолеты/ГЖ/new_eng_china.xls")
print("Не забудь скопировать новые названия в старый файл")
book.save("/root/Yandex.Disk/самолеты/ГЖ/A290/PU_Ukraine_.07-290-93.xls")
