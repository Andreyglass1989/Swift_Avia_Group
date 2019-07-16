from LK.models import Pack

pack = Pack.objects.filter(pack_status=1, sklad_id=1, total__gt=1, total__lte=150).exclude(customer_id=0)
len(pack)

for p in pack:
	print(p.pack_id, p.pack_number, p.weight, p.total, p.customer.external_id)

'''
#for 1 pack - 1 parcel
Pack.objects.filter(total__gt=1)

'''