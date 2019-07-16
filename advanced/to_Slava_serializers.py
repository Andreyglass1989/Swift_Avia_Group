from LK.models import Parcel, Pack, ParcelPackProduct
# from rest_framework import serializers
from django.http import JsonResponse
import json


def pack_today(date):
	q = Parcel.objects.filter(date_added__contains = date, parcel_status_id=2)
	# for zz in q:
	# 	z = Pack.objects.filter(parcelpackproduct__parcel_id)

	pack_today=[]
	full_data = []


	for n in q:
		p = ParcelPackProduct.objects.filter(parcel_id=n.parcel_id).first()
		if p.pack_id not in pack_today:
			pack_today.append(p.pack_id)


	for p in pack_today:
		data = Pack.objects.get(pack_id=p)
		parcel_number=[]
		dict_00 = {"date": data.date_added.strftime("%Y-%m-%d"),
				   "weight": data.weight,
				   "customer": data.customer.external_id,
				   "comment": data.comment,
				   "group": data.category_group.category_group_id, 
		}

	 	# print(p, data.date_added.strftime("%Y-%m-%d"), data.weight, data.customer.external_id, data.comment, data.category_group.category_group_id)		
		parcel = Parcel.objects.filter(parcelpackproduct__pack_id=data.pack_id).order_by('parcel_id')
		for z in parcel:
			if z.external_id not in parcel_number:
				parcel_number.append(z.external_id)
				# print(z.external_id)
		dict_00['parcel'] = parcel_number
		full_data.append(dict_00)
	return JsonResponse(full_data, safe=False)

	# response = JsonResponse(full_data, safe=False)
	# d = json.loads(response.content)
	# return d



list = ['a', 'b', 'c']
dict={}

dict['full'] = list