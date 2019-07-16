# -*- coding: utf-8 -*-
from LK.models import Parcel, Pack, ParcelPackProduct
import xlrd, xlwt
import datetime

d = datetime.datetime.now()

q = Parcel.objects.filter(date_added__contains = d.strftime("%Y-%m-%d"), parcel_status_id=2)
# q = Parcel.objects.filter(date_added__contains = '2019-07-04', parcel_status_id=2)


pack_today=[]
parcel_number=[]


""" for exel """
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 0, "Дата захода")
sheet1.write(0, 1, "код клиента")
sheet1.write(0, 2, "вес")
sheet1.write(0, 3, "кол-во мест")
sheet1.write(0, 4, "пломбы (места)")
sheet1.write(0, 5, "НАИМЕНОВАНИЕ")
sheet1.write(0, 6, "треки")
sheet1.write(0, 7, "комментарий")

i=0
""" for exel """

for n in q:	
	print(n.parcel_number)
	p = ParcelPackProduct.objects.filter(parcel_id=n.parcel_id).first()
	try:
		if p.pack_id not in pack_today:
			print(p)
			pack_today.append(p.pack_id)
	except AttributeError:
		print("None")


for p in pack_today:

	i = i+1

	data = Pack.objects.get(pack_id=p)
 	print(p, data.date_added.strftime("%Y-%m-%d"), data.weight, data.customer.external_id, data.comment)		
 	
 	sheet1.write(i, 0, data.date_added.strftime("%Y-%m-%d"))
 	sheet1.write(i, 1, data.customer.external_id)
 	sheet1.write(i, 2, data.weight)
 	sheet1.write(i, 3, '')
 	sheet1.write(i, 5, '')
 	sheet1.write(i, 6, data.comment)
 	# print()
 	if data.category_group.category_group_id == 21:
 		sheet1.write(i, 7, "красным")
 	else:
 		sheet1.write(i, 7, "")

	parcel = Parcel.objects.filter(parcelpackproduct__pack_id=data.pack_id).order_by('parcel_id')
	for z in parcel:
		if z.external_id not in parcel_number:
			parcel_number.append(z.external_id)
			print(z.external_id)
			sheet1.write(i, 4, z.external_id)
			i=i+1



book.save("/root/Yandex.Disk/самолеты/ГЖ/A266/A266_auto.xls")