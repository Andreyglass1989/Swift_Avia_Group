from LK.models import Parcel, Pack, ParcelPackProduct
from rest_framework import serializers

q = Parcel.objects.filter(date_added__contains = '2019-01-03', parcel_status_id=2)

pack_today=[]
parcel_number=[]

for n in q:
	p = ParcelPackProduct.objects.filter(parcel_id=n.parcel_id).first()
	if p.pack_id not in pack_today:
		pack_today.append(p.pack_id)


for p in pack_today:
	data = Pack.objects.get(pack_id=p)
 	print(p, data.date_added.strftime("%Y-%m-%d"), data.weight, data.customer.external_id, data.comment, data.category_group.category_group_id)		
	parcel = Parcel.objects.filter(parcelpackproduct__pack_id=data.pack_id).order_by('parcel_id')
	for z in parcel:
		if z.external_id not in parcel_number:
			parcel_number.append(z.external_id)
			print(z.external_id)
