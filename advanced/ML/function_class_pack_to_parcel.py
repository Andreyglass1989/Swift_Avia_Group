# _*_ coding: utf-8 _*_
from LK.models import (
	Parcel,
  	ParcelPackProduct,
  	PackProduct,
  	Pack,
  	PackStatus,
  	ExternalId,
  	PartnerInc2Sandbox
 )

def change_pack_field(pack):
	pack.pack_status_id = 2
	if pack.currency_id == 0:
		pack.currency_id = 2
	pack.save()

def create_new_external_id():
	ExternalId.objects.create()
	parcel_external_id = ExternalId.objects.last().autoinc_id
	return parcel_external_id

def create_new_parcel_number():
	number_part0 = int(PartnerInc2Sandbox.objects.last().number)+1
	PartnerInc2Sandbox.objects.create(number=str(number_part0))
	parcel_num = PartnerInc2Sandbox.objects.last().number
	return parcel_num


def pack1_1_1(num_pack):
	# 1 место 1 посылка
	pack = Pack.objects.get(pack_number=num_pack)
	parcel_external_id = create_new_external_id()
	parcel_num = create_new_parcel_number()
	new_parcel = Parcel(parcel_number=str(parcel_num), parcel_status=PackStatus.objects.get(pack_status_id=2), sklad_id=1, weight=pack.weight, 
						weight_b=float(0.00), point=1, total=pack.total, 
						external_id=parcel_external_id, volume=pack.volume, 
						width=float(0.00), height=float(0.00), length=float(0.00), comment="", sandbox=0)
	new_parcel.save()
	new_parcel_pack_product = ParcelPackProduct(parcel=new_parcel, pack_product=PackProduct.objects.get(pack_id=pack.pack_id), pack=pack, 
												quantity=pack.products.first().quantity, weight=float(0.00), point=1, loss=0)
	new_parcel_pack_product.save()
	change_pack_field(pack)


#1место*1продукт*Nпосылок
def pack1_1_n(num_pack):
	pack = Pack.objects.get(pack_number=num_pack)
	x = divmod(pack.total, 100.0)
	if x[1]>0:
		num_parcel = int(x[0]+1)
		zzz = divmod(pack.products.first().quantity, num_parcel)
		if zzz[1] == 0:
#логика формирования посылок
			prcl_weight = round(pack.weight/num_parcel, 2)
			prcl_volume = round(pack.volume/num_parcel, 5)
			parcel_external_id = create_new_external_id()
			for i in range(1, num_parcel+1):
				print(i)
				parcel_num = create_new_parcel_number()
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
			prcl_weight = round(pack.weight/num_parcel, 2)
			prcl_volume = round(pack.volume/num_parcel, 5)
			parcel_external_id = create_new_external_id()
			for i in range(1, num_parcel+1):
				parcel_num = create_new_parcel_number()
				if i<num_parcel:
					print(i, "True")
					# x = z
					new_parcel = Parcel(parcel_number=str(parcel_num), parcel_status=PackStatus.objects.get(pack_status_id=2), sklad_id=1, weight=prcl_weight, 
										weight_b=float(0.00), point=1, total = round(pack.products.first().price*zzz[0], 2), 
										external_id=parcel_external_id, volume=prcl_volume, 
										width=float(0.00), height=float(0.00), length=float(0.00), comment="", sandbox=0)
					new_parcel.save()
					new_parcel_pack_product = ParcelPackProduct(parcel=new_parcel, pack_product=pack.products.first(), pack=pack, 
														quantity=zzz[0], weight=float(0.00), point=1, loss=0)
					new_parcel_pack_product.save()
				elif i == num_parcel:
					print(i, "last")

		# print(zzz)
		change_pack_field(pack)
		
	elif x[1] == 0:
		x = divmod(pack.total, 100.0)
		print(x)
		if x[1] == 0:
			num_parcel = int(x[0])
			print(num_parcel)
			zzz = divmod(pack.products.first().quantity, num_parcel)
			if zzz[1] == 0:
		#логика формирования посылок
				prcl_weight = round(pack.weight/num_parcel, 2)
				prcl_volume = round(pack.volume/num_parcel, 5)
				print(prcl_volume, prcl_weight)
				parcel_external_id = create_new_external_id()
				# print("total =", round(pack.products.first().price*zzz[0], 2))
				for i in range(1, num_parcel+1):
					parcel_num = create_new_parcel_number()
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











#Nмест*1продукт*Nпосылок
def packn_1_n(num_pack):
	pack = Pack.objects.get(pack_number=130272845)
	x = divmod(pack.total, 100.0)
	if x[1]<10:
		num_parcel = int(x[0])
		zzz = divmod(pack.products.first().quantity, num_parcel)
		print(zzz)
		if zzz[1] == 0:
	#логика формирования посылок
			prcl_weight = round(pack.weight/num_parcel, 2)
			prcl_volume = round(pack.volume/num_parcel, 5)
			print(prcl_volume, prcl_weight)
			# print("total =", round(pack.products.first().price*zzz[0], 2))
			for i in range(1, num_parcel+1):
				parcel_external_id = create_new_external_id()
				parcel_num = create_new_parcel_number()
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