from LK.models import (
	# PlombaDimension,
	Parcel,
	ParcelPackProduct,
	Pack,
	PackProduct,
    )
import xlrd, xlwt



rb = xlrd.open_workbook('CHECKLIST1.xls',formatting_info=False)
sheet = rb.sheet_by_index(0)

#32327
j=33142

for rownum in range(sheet.nrows):
	row = sheet.row_values(rownum)
	print(int(row[3]), row[6], float(row[7]))
	ppp = PackProduct.objects.get(pack_product_id=j)
	ppp.price=float(row[7])
	#p=PackProduct.objects.create(pack_product_id=j, pack_id=10073, name=row[6] , price=float(row[8]), quantity=int(row[3]), item_class_id=3, weight=0.001, weight_netto=0.2, volume=0.001, point=1, packed_quantity=0, url='')
	j = j+1
	ppp.save()

int(row[1])
#str(row[0])



rb = xlrd.open_workbook('CHECKLIST.xls',formatting_info=False)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
	row = sheet.row_values(rownum)
	print(row)
	ppp = Parcel.objects.get(parcel_number=int(row[0]))
	z = ParcelPackProduct.objects.get(parcel_id=ppp.parcel_id)#.update(quantity=row[1])
	z.quantity = int(row[1])
	# if row[3] == '':
	# 	ppp.weight = ppp.weight
	# 	z.quantity = int(row[1])
	# 	ppp.total = float(row[2])
		
	# elif row[2] == '':
		# ppp.total = float(row[2])
		# ppp.weight = float(row[3])
		# print(type(row[2]))
		# print(type(row[3]))
	# elif row[2] == '' and row[3] =='':
	# 	print('nothing')	
	# else:
	# 	ppp.weight = float(row[3])
	# 	ppp.total = float(row[2])

	z.save()
	#ppp.save()	


	if row[3] == '' and row[4] == '' and row[5] == '':
		#print("True", row[3], row[4], row[5])
		#print(row[0], type(row[1]))
		a = int(Decimal(row[1]))
		print(a, row[3], row[4], row[5], row[2])
		print(type(a))
	elif row[3] != '' and row[4] != '' and row[5] != '':
		print("not None")
		PlombaDimension.objects.create(plomba_id=int(Decimal(row[1])), plomba_width=row[3], plomba_height=row[4], plomba_length=row[5], plomba_weight=row[2])
		#print(int(Decimal(row[1])), row[3], row[4], row[5], row[2])

# for c_el in row:
# print c_el

#PlombaDimension.objects.create(plomba_id=61195, plomba_width=70, plomba_height=68, plomba_length=33, plomba_weight=31.35)



# pl=Parcel.objects.get(external_id=61937)
# pl.width = 68
# pl.height = 70
# pl.length = 33
# pl.weight_b = 31.35
# pl.save()
