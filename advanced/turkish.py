from LK.models import (	Address, AirParcel )

list69=[]
list70=[]
list71=[]

p = Address.objects.filter(category_id=69)
for p1 in p:
	list69.append(p1.address_id)

p = Address.objects.filter(category_id=70)
for p1 in p:
	list70.append(p1.address_id)

p = Address.objects.filter(category_id=71)
for p1 in p:
	list71.append(p1.address_id)

---------------------------------------------
list12=[]
p = Address.objects.filter(category_id=12)
for p1 in p:
	list12.append(p1.address_id)


----------------------------------------

#list = list69 + list70+list71

#fl = AirParcel.objects.filter(air_id=290)

i=0
j=82718

for f in list12:
	print(list12[i])
	#print(AirParcel.objects.filter(address_id=list[i]))
	AirParcel.objects.filter(air_id=290, address_id=23616, air_parcel_id=j).update(address_id=list12[i])
	
	#f.update(address_id=list[i])
	i=i+1
	j=j+1
