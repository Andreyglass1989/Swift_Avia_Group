# -*- coding: utf-8 -*-
from LK.models import Parcel, Pack, ParcelPackProduct
from login.models import UserProfile

q = Parcel.objects.get(parcel_number = 130264583)
p = ParcelPackProduct.objects.get(parcel_id=q.parcel_id)
data = Pack.objects.get(pack_id=p.pack_id)

print(data.customer)
------------------------------

