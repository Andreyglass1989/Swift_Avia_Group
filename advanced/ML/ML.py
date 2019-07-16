# -*- coding: utf-8 -*-
from LK.models import Pack, PackProduct, Parcel
import datetime

features = []
list0 = []
labels = []


# обimport pickleучаем модель на данных
# pack = Pack.objects.filter(date_added__gt = datetime.date(2019, 6, 1)).exclude(sklad_id__in=[3,5,6]).exclude(customer_id=0).exclude(pack_status_id=1)#, pack_status_id = 1
# for pc in pack:
# 	list0 = [pc.customer, pc.pack_number, pc.point, pc.total, pc.weight, pc.volume, pc.products.count(), pc.parcelpackproduct_set.count()]
# 	# print(list0)
# 	features.append(list0)
# 	if pc.total<=110 and pc.point == 1 and pc.products.count()==1 and pc.parcelpackproduct_set.count()==1:
# 		# pass
# 		labels.append(1)
# 		print(1)
# 	elif pc.total<=110 and pc.point == pc.products.count() and pc.products.count()>1 and pc.parcelpackproduct_set.count() == 1:
# 		labels.append(2)
# 		print(2)
# 	elif pc.point == 1 and pc.products.count()>=1 and pc.parcelpackproduct_set.count() > 1:
# 		labels.append(3)
# 		print(3)
# 	elif pc.point == pc.products.count() and pc.point == pc.parcelpackproduct_set.count() and pc.products.count() == pc.parcelpackproduct_set.count():
# 		labels.append(4)
# 		print(4)
# 	elif pc.point == pc.parcelpackproduct_set.count() and pc.products.count() == 1:
# 		labels.append(5)
# 		print(5)
# 	else:
# 		print(list0)
# 		labels.append(0)
# 		print(0)

x0=0
x1=0
x2=0
x3=0
x4=0
x5=0


pack = Pack.objects.filter(date_added__gt = datetime.date(2019, 6, 1)).exclude(sklad_id__in=[3,5,6]).exclude(customer_id=0).exclude(pack_status_id=1)#, pack_status_id = 1
for pc in pack:
	list0 = [pc.point, pc.total, pc.weight, pc.volume, pc.products.count()] #pc.customer, pc.pack_number, 
	print(list0)
	features.append(list0)
	if pc.total<=110 and pc.point == 1 and pc.products.count()==1:
		# pass
		labels.append(1)
		x1 +=1
		print(1, pc.parcelpackproduct_set.count())
	elif pc.total<=110 and pc.point == pc.products.count() and pc.products.count()>1:
		labels.append(2)
		print(2, pc.parcelpackproduct_set.count())
	elif pc.point == 1 and pc.products.count()==1 and pc.total>110:
		labels.append(3)
		print(3, pc.parcelpackproduct_set.count())
		x3+=1
	elif pc.point == pc.products.count() and pc.point>1 and pc.total>110:
		labels.append(4)
		print(4, pc.parcelpackproduct_set.count())
		x4+=1
	elif pc.products.count() == 1 and pc.total>110 and (pc.point*100)+(pc.point*10)>=pc.total>(pc.point-1)*100:
		labels.append(5)
		print(5, pc.parcelpackproduct_set.count())
		x5+=1
	else:
		print(list0)
		labels.append(0)
		print(0, pc.parcelpackproduct_set.count())
		x0+=1
print(pack.count(), x0, x1, x2, x3, x4, x5)

# предсказываем как модели классифицировать
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)


#сохраняем модель в файл
import pickle
# now you can save it to a file
with open('model_pack_to_parcel_13_07.pkl', 'wb') as f:
    pickle.dump(clf, f)



# print(clf.predict([[200, 1]]))
# clf.predict([[1, 4, 0.1, 0.0026, 1]])

#сохраняем в exel файл наши данные

from LK.models import Pack
import datetime

features_parcel = []
list0_parcel = []
labels_parcel = []

# обучаем модель на данных
pack = Pack.objects.filter(date_added__gt = datetime.date(2019, 6, 15)).exclude(sklad_id__in=[3,5,6]).exclude(customer_id=0).exclude(pack_status_id=1)#, pack_status_id = 1 ,  date_added__icontains = "2019-06"

for pc in pack:
	list0_parcel = [pc.point, pc.total, pc.weight, pc.volume, pc.products.count()]
	print(list0_parcel)
	print(pc.parcelpackproduct_set.count())
	features_parcel.append(list0_parcel)
	labels_parcel.append(pc.parcelpackproduct_set.count())
"""
1 место 1 продукт 1 посылка - 1
1 место N продуктов 1 посылка - 2
1 место 1 продукт N посылок - 3
N мест = N продукт = N посылок  - 4
N мест = N посылок 1 продукт - 5

"""


"""
import pickle
# now you can save it to a file
with open('filename.pkl', 'wb') as f:
    pickle.dump(clf, f)

# and later you can load it
with open('filename.pkl', 'rb') as f:
    clf = pickle.load(f)
"""