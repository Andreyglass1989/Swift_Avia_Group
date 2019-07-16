# -*- coding: utf-8 -*-
from LK.models import (
	AirParcel,
	Parcel,
	Address,
  ParcelPackProduct,
  PackProduct,
    )
import xlrd, xlwt
from django.core.exceptions import ObjectDoesNotExist

a=[]
# list_repeat = []

rb = xlrd.open_workbook('/root/Yandex.Disk/самолеты/ГЖ/A290/docs/man-290.xls',formatting_info=False)
#rb = xlrd.open_workbook('/root/Yandex.Disk/самолеты/Санька/TURKISH/T01_manifest_norm.xls',formatting_info=False)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
  row = sheet.row_values(rownum)
  #parcelNumber = re.compile(r'\d')

  if isinstance(row[0], float):
#    print(row[0])
    if int(row[0]) not in a:
      a.append(int(row[0]))
    else:
      print(row[0])
    # else:
    #   list_repeat.append(int(row[0]))

print(len(a))


d = { 3480: 'Cherkassi', 3481: 'Chernigov',
      3482: 'Chernovtsu', 3483: 'Krim',
      3484: 'Dnepropetrovsk', 3485: 'Donetsk',
      3486: 'Ivano-Frankovsk', 3487: 'Kherson',
      3488: 'Khmelnitskij', 3489: 'Kirovograd',
      3490: 'Kiev', 3491: 'Kievskaya oblast',
      3492: 'Lugansk', 3493: 'Lviv',
      3494: 'Nikolaev', 3495: 'Odessa',
      3496: 'Poltava', 3497: 'Rovno',
      3498: 'Sevastopol', 3499: 'Sumu',
      3500: 'Ternopol', 3501: 'Vinnitsa',
      3502: 'Lutsk', 3503: 'Uzhgorod',     
      3504: "Zaporozh'e", 3505: 'Zhitomir',
      4224: 'Kharkiv'
}

new_a=[]
for c in a:
	if c not in new_a:
		new_a.append(c)
len(new_a)

'''
не хватает 2-х посылок
'''
air_id=348
list0=[]
list1=[]

p = AirParcel.objects.filter(air_id=air_id)
for z in p:
	print(z.parcel_id)
	list0.append(z.parcel_id)
'''
получили список parcel_id
теперь нужно получить parcel_number из табл.Parcel:
'''
for zzz in list0:
  ppp=Parcel.objects.get(parcel_id=zzz)
  list1.append(int(ppp.parcel_number))

list1

'''
поиск и удаление повторяющихся номеров уп
'''
list2=[]
for z in a:
  if z not in list2:
    list2.append(z)
list3=list(set(list1)-set(list2)) 

"""
---------------------------------------------------------------------------------------
Вага и вартисть
"""
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 0, "номер посылки")
sheet1.write(0, 1, "Найменування")
sheet1.write(0, 3, "вага")
sheet1.write(0, 4, "стоимость")
sheet1.write(0, 6, "Одержувач МЕВ")
sheet1.write(0, 8, "адреса одержувача")

i=0
#addd
list_parcel_id=[]
#add
for z in new_a:
  print(z)
  p = Parcel.objects.get(parcel_number=z, sklad_id=1)
  i = i+1
  ##  формируем parcel_id
  list_parcel_id.append(p.parcel_id)
  #
  sheet1.write(i, 0, z)
  sheet1.write(i, 4, p.total)
  sheet1.write(i, 3, p.weight)

#  формируем adress_id
list_adress_id=[]
i=1
for a00 in list_parcel_id:
  #print(a00)
  aa = AirParcel.objects.filter(parcel_id=a00).first()
  list_adress_id.append(aa.address_id) 
  #формируем наименования
  # aaa = ParcelPackProduct.objects.filter(parcel_id=a)
  # if len(aaa) == 1:
  #   for a0 in aaa:
  #     p = PackProduct.objects.get(pack_product_id=a0.pack_product_id)
  #     print(p.name)
  #     sheet1.write(i, 1, p.name)
  #     i=i+1

#имя + фамилия 
i = 0
for name in list_adress_id:
    try: 
      nn = Address.objects.get(address_id=name)
      i = i+1
      sheet1.write(i, 6, nn.firstname + " " + nn.lastname)
      sheet1.write(i, 8, unicode(d.get(nn.zone_id)) + "  " + unicode(nn.city) + ", " + unicode(nn.address_1) + " " + str(nn.dom))
    except ObjectDoesNotExist:
      i = i+1
      sheet1.write(i, 6, "NONAME")
      sheet1.write(i, 8, "HELLO WORLD")



book.save("/root/Yandex.Disk/самолеты/ГЖ/A290/docs/little_help_290.xls")