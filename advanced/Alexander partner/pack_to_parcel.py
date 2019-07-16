# _*_ coding: utf-8 _*_
from LK.models import (
	Parcel,
  	ParcelPackProduct,
  	PackProduct,
  	Pack,
  	PackStatus,
  	ExternalId, 
  	PartnerInc0Sandbox
 )

def change_pack_field(pack):
	pack.pack_status_id = 2
	if pack.currency_id == 0:
		pack.currency_id = 2
	pack.save()


def pack1_1():
	# 1 место 1 посылка
	pack1_1 = Pack.objects.filter(pack_status=1, sklad_id=1, point=1, total__gt=1, total__lte=102).exclude(customer_id=0).exclude(category_group__in=[20,21])
	for pack in pack1_1: 
		ExternalId.objects.create()
		parcel_external_id = ExternalId.objects.last().autoinc_id
		number_part0 = int(PartnerInc0Sandbox.objects.last().number)+1
		PartnerInc0Sandbox.objects.create(number=str(number_part0))
		parcel_num = PartnerInc0Sandbox.objects.last().number
		new_parcel = Parcel(parcel_number=str(parcel_num), parcel_status=PackStatus.objects.get(pack_status_id=2), sklad_id=1, weight=pack.weight, 
							weight_b=float(0.00), point=1, total=pack.total, 
							external_id=parcel_external_id, volume=pack.volume, 
							width=float(0.00), height=float(0.00), length=float(0.00), comment="", sandbox=0)
		new_parcel.save()
		new_parcel_pack_product = ParcelPackProduct(parcel=new_parcel, pack_product=PackProduct.objects.get(pack_id=pack.pack_id), pack=pack, 
													quantity=pack.products.first().quantity, weight=float(0.00), point=1, loss=0)
		new_parcel_pack_product.save()
		change_pack_field(pack)



def pack1_n():
	#Для 1 до (100$) посылки несколько продуктов
	pack1_n = Pack.objects.filter(pack_status=1, sklad_id=1, point__gt=1, total__gt=1, total__lte=102).exclude(customer_id=0).exclude(category_group__in=[20,21])

	for pack in pack1_n:
		ExternalId.objects.create()
		parcel_external_id = ExternalId.objects.last().autoinc_id
		parcel_num = int(Parcel.objects.all().last().parcel_number)+1
		PartnerInc0Sandbox.objects.create(number=str(parcel_num))
		new_parcel = Parcel(parcel_number=str(parcel_num), parcel_status=PackStatus.objects.get(pack_status_id=2), sklad_id=1, weight=pack.weight, 
						weight_b=float(0.00), point=1, total=pack.total, 
						external_id= parcel_external_id, volume=pack.volume, 
						width=float(0.00), height=float(0.00), length=float(0.00), comment="", sandbox=0)
		new_parcel.save()
		for prod in pack.products.all():
			new_parcel_pack_product = ParcelPackProduct(parcel=new_parcel, pack_product=PackProduct.objects.get(pack_product_id=prod.pack_product_id), pack=pack,
														quantity=prod.quantity, weight=float(0.00), point=1, loss=0)
			new_parcel_pack_product.save()

		# pack.pack_status_id = 2
		change_pack_field(pack)




#посылка-место-товар(до 100$)
packn_n = Pack.objects.filter(pack_status=1, sklad_id=1, point__gt=1, total__gt=1).exclude(customer_id=0).exclude(category_group__in=[20,21])
# print(pack)
for pack in packn_n:
	#посылка-место-товар
	if pack.products.count() == pack.point:
		for products in pack.products.all():
			if products.price*products.quantity <= 101:
				ExternalId.objects.create()
				prcl_weight = round(pack.weight/pack.point, 2)
				prcl_volume = round(pack.volume/pack.point, 5)
				# print(prcl_weight, prcl_volume, products.price*products.quantity, i)
				parcel_external_id = ExternalId.objects.last().autoinc_id
				parcel_num = int(Parcel.objects.all().last().parcel_number)+1
				PartnerInc0Sandbox.objects.create(number=str(parcel_num))
				new_parcel = Parcel(parcel_number=str(parcel_num), parcel_status=PackStatus.objects.get(pack_status_id=2), sklad_id=1, weight=prcl_weight, 
									weight_b=float(0.00), point=1, total = products.price*products.quantity, 
									external_id=parcel_external_id, volume=prcl_volume, 
									width=float(0.00), height=float(0.00), length=float(0.00), comment="", sandbox=0)
				new_parcel.save()
				new_parcel_pack_product = ParcelPackProduct(parcel=new_parcel, pack_product=products, pack=pack, 
													quantity=pack.products.first().quantity, weight=float(0.00), point=1, loss=0)
				new_parcel_pack_product.save()
				if pack.pack_status_id == 1:
					change_pack_field(pack)

			else:
				continue
				print("Не подходит для упаковки инвойс больше 100 у.е.")
				# pass
		
	else:
		print(pack, False)
		pass




#1место*1продукт*Nпосылок
pack1_1_n = Pack.objects.filter(pack_status=1, sklad_id=1, point=1, total__gt=102).exclude(customer_id=0).exclude(category_group__in=[20,21])
for pack in pack1_1_n:
	print(pack.total)
	x = divmod(pack.total, 100.0)
	if x[1]>0:
		print(pack)
		num_parcel = int(x[0]+1)
		print(num_parcel)
		zzz = divmod(pack.products.first().quantity, num_parcel)
		if zzz[1] == 0:
#логика формирования посылок
			ExternalId.objects.create()
			prcl_weight = round(pack.weight/num_parcel, 2)
			prcl_volume = round(pack.volume/num_parcel, 5)
			print(prcl_volume, prcl_weight)
			parcel_external_id = ExternalId.objects.last().autoinc_id
			# print("total =", round(pack.products.first().price*zzz[0], 2))
			for i in range(1, num_parcel+1):
				parcel_num = int(Parcel.objects.all().last().parcel_number)+1
				# print("parcel number=", parcel_num+i)
				new_parcel = Parcel(parcel_number=str(parcel_num), parcel_status=PackStatus.objects.get(pack_status_id=2), sklad_id=1, weight=prcl_weight, 
									weight_b=float(0.00), point=1, total = round(pack.products.first().price*zzz[0], 2), 
									external_id=parcel_external_id, volume=prcl_volume, 
									width=float(0.00), height=float(0.00), length=float(0.00), comment="", sandbox=0)
				new_parcel.save()
				new_parcel_pack_product = ParcelPackProduct(parcel=new_parcel, pack_product=pack.products.first(), pack=pack, 
													quantity=zzz[0], weight=float(0.00), point=1, loss=0)
				new_parcel_pack_product.save()
#логика формирования посылок
		else:
			pass
		# print(zzz)
	elif x[1] == 0:
		x = divmod(pack.total, 100.0)
		print(x)
		if x[1] == 0:
			num_parcel = int(x[0])
			print(num_parcel)
			zzz = divmod(pack.products.first().quantity, num_parcel)
			if zzz[1] == 0:
		#логика формирования посылок
				ExternalId.objects.create()
				prcl_weight = round(pack.weight/num_parcel, 2)
				prcl_volume = round(pack.volume/num_parcel, 5)
				print(prcl_volume, prcl_weight)
				parcel_external_id = ExternalId.objects.last().autoinc_id
				# print("total =", round(pack.products.first().price*zzz[0], 2))
				for i in range(1, num_parcel+1):
					parcel_num = int(Parcel.objects.all().last().parcel_number)+1
					# print("parcel number=", parcel_num+i)
					new_parcel = Parcel(parcel_number=str(parcel_num), parcel_status=PackStatus.objects.get(pack_status_id=2), sklad_id=1, weight=prcl_weight, 
										weight_b=float(0.00), point=1, total = round(pack.products.first().price*zzz[0], 2), 
										external_id=parcel_external_id, volume=prcl_volume, 
										width=float(0.00), height=float(0.00), length=float(0.00), comment="", sandbox=0)
					new_parcel.save()
					new_parcel_pack_product = ParcelPackProduct(parcel=new_parcel, pack_product=pack.products.first(), pack=pack, 
														quantity=zzz[0], weight=float(0.00), point=1, loss=0)
					new_parcel_pack_product.save()
		change_pack_field(pack)

		# print(pack)
	else:
		print("Третий вариант!")
		print(pack)




round(196.8/100, 0)


















# p = Pack.objects.get(products__point=1)

# if (p.products.count() for p in Pack.objects.filter(pack_status=1, sklad_id=1, point__gt=1, total__gt=102).exclude(customer_id=0).exclude(category_group=20))==1:
# 	print("True")
# else:
# 	print("False")




# pack = Pack.objects.filter(pack_status=1, sklad_id=1, point__gt=1, total__gt=102, products__point__gt=1).exclude(customer_id=0).exclude(category_group=20)
# list1=[p.products.count() for p in Pack.objects.filter(pack_status=1, sklad_id=1, point__gt=1, total__gt=102).exclude(customer_id=0).exclude(category_group=20)]

# In [4]: for p in pack1_1:
#    ...:     print(p.products.all().count())
