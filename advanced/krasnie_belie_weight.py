from LK.models import Pack

obj = Pack.objects.filter(pack_status=2, sklad=1, category_group=3)
weight = 0
volume = 0
for w in obj:
	weight = weight+w.weight
	volume = volume+w.volume
print("Prostie=", weight, volume)

obj2 = Pack.objects.filter(pack_status=2, sklad=1, category_group=21)
weight1 = 0
volume1 = 0
for w in obj2:
	weight1 = weight1+w.weight
	volume1 =  volume1+w.volume 
print("Krasnih=", weight1, volume1)