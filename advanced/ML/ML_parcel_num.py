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

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_parcel, labels_parcel)
# print(clf.predict([[5, 1250, 112.5, 0.15, 1]]))

with open('count_parcel_number.pkl', 'rb') as f:
    clf_parcel_num = pickle.load(f)
#сохраняем обучееную модель в файл
import pickle
# now you can save it to a file
with open('count_parcel_number.pkl', 'wb') as f:
    pickle.dump(clf, f)