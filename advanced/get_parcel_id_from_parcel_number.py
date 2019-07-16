from LK.models import (
	# PlombaDimension,
	Parcel,
	ParcelPackProduct,
	Pack,
	PackProduct,
    )
import xlrd, xlwt


rb = xlrd.open_workbook('CHECKLIST.xls',formatting_info=False)
sheet = rb.sheet_by_index(0)

for rownum in range(sheet.nrows):
	row = sheet.row_values(rownum)
	p=Parcel.objects.get(parcel_number=int(row[0]))
	print(p.parcel_id)
