# -*- coding: utf-8 -*-
import pickle
from LK.models import Pack, PackProduct, Parcel
import datetime
from function_class_pack_to_parcel import pack1_1_1, pack1_1_n

# and later you can load it
with open('model_pack_to_parcel_13_07.pkl', 'rb') as f:
    clf = pickle.load(f)

x0=0
x1=0
x3=0
x5=0

#получаем посылки которые на складе не разбитые и нужно их разбить
pack = Pack.objects.filter(sklad_id = 1, pack_status_id = 1, total__gt=1).exclude(customer_id=0).exclude(category_group__in=[20,21])
for pk in pack:
	#предсказываем какое к-во посылок необходимо
	# parcel_num = clf_parcel_num.predict([[pk.point, pk.total, pk.weight, pk.volume, pk.products.count()]])
	# print(parcel_num[0])
	#предсказываем к какому классу данный упаковочный будет принадлежать
	pack_class = clf.predict([[pk.point, pk.total, pk.weight, pk.volume, pk.products.count()]])
	print(pack_class)
	print(pk.pack_number)
	#1 место 1 продукт 1 посылка - 1
	if pack_class[0] == 1:
		# pack1_1_1(pk.pack_number)
		print(" function pack1_1_1", pk.pack_number)
		x1+=1
	# 1 место 1 продукт N посылок - 3
	elif pack_class[0] == 3:
		print(" function pack1_1_n", pk.pack_number)
		x3+=1
		# pack1_1_n(pk.pack_number)
	elif pack_class[0] == 5:
		print(" function packn_1_n", pk.pack_number)
		x5+=1
	else:
		x0+=1
		print("I didn't know how!!")