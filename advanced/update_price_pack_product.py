from LK.models import (
	PackProduct,
	Parcel,
	ParcelPackProduct,
    )
import xlrd, xlwt

rb = xlrd.open_workbook('CHECKLIST.xls',formatting_info=False)
sheet = rb.sheet_by_index(0)

for rownum in range(sheet.nrows):
	row = sheet.row_values(rownum)
	print(row)

	p = ParcelPackProduct.objects.get(parcel_id=int(row[1]))
	p.pack_product_id = int(row[2])
	p.pack_id = 9939
	p.quantity = int(row[3])
	p.save()

	parcel = Parcel.objects.get(parcel_id=int(row[1]))
	parcel.total = float(row[4])
	parcel.save()
	# pack_prod = PackProduct.objects.get(pack_product_id=int(row[3]))
	# pack_prod.price = row[2]
	# pack_prod.save()
