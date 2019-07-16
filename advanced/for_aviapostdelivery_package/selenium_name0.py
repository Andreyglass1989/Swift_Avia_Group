# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LK.models import Pack, Parcel, ParcelPackProduct, Customer
from datetime import datetime
import pandas as pd
import time


capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = True
binary = FirefoxBinary('/root/FireFox/firefox/firefox')
driver = webdriver.Firefox(firefox_binary=binary)
#driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)

driver = webdriver.Firefox()

#---вход в систему
driver.get('http://aviapostdelivery.com/admin/index.php?route=sale/pack')
linkElem_username=driver.find_element_by_name('username')
linkElem_pass=driver.find_element_by_name('password')

linkElem_username.send_keys('aUkraine')
linkElem_pass.send_keys('fw94kqmd020JJddeW')
linkElem_pass.submit()
# фокусируем на начало сверху экрана
WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.ID, "overley")))
driver.execute_script("window.scrollTo(0, 450)")


def click_button_plus(pack_id, pack_product_id):
	a = "button[pack-id='{0}']".format(pack_id)
	driver.find_element_by_css_selector(a).click()
	b = "input[value='{0}']".format(pack_product_id)
	driver.find_element_by_css_selector(b).click()
	return "Готово!"
#------------------------------------------------

answer = 'y'

# for 1 pcs - 1 parcel
pack = Pack.objects.filter(pack_status=1, sklad_id=1, point=1, total__gt=1, total__lte=102).exclude(customer_id=0).exclude(category_group=20)
print(pack)

for p in pack:
	print(p.pack_id, p.pack_number, p.weight, p.total, p.customer.external_id)
	# if answer =='y':
# while answer != 'n':
	a = "input[type='checkbox'][name='selected[]'][value='{0}']".format(p.pack_id)
	# driver.find_elements_by_xpath("//*/table/tbody/tr/td/input[type='checkbox'][name='selected[]'][value='']")
	print(a)
	element = driver.find_element_by_css_selector(a)
	# driver.implicitly_wait(10)
	print(element)
	# webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
	element.click()

	driver.implicitly_wait(10)
	driver.find_element_by_css_selector("input#parcel-weight").send_keys(str(p.weight))
	driver.find_element_by_css_selector("input#parcel-volume").send_keys(str(p.volume))

	driver.find_element_by_class_name('parcel').click()
	driver.back()
		# answer = raw_input("Продолжить? y/n ")
	# elif answer=='n':
	# 	break


# 1 место - от 2-х и более посылок (один товар)
pack = Pack.objects.filter(pack_status=1, sklad_id=1, point=1, total__gt=150, weight__gt=1, weight__lt=30).exclude(customer_id=0).exclude(category_group=20)
print(pack, len(pack))


for p in pack:
	if len(p.products.all())==1:
		total_pack = p.total
		product = p.products.first()
		product_quantity = product.quantity
		print(total_pack, product_quantity)
		raw_input("Пока я не научился разбивать посылки как нужно, помоги мне, а тебе ;)")
		click_button_plus(p.pack_id, product.pack_product_id)

		# print(p.total, quant_parcel)








# для текстиля, для пленок 1 к-во - 1 место
pack = Pack.objects.filter(pack_status=1, sklad_id=1, point__gt=1, total__gt=150).exclude(customer_id=0).exclude(category_group=20)

len(pack)
print(pack)
# фильтруем упаковочные
for p in pack:
    # if len(p.products.all()) > 1:
    #     print("No its more",  p.pack_number, p.products.all().first().name, len(p.products.all()))
    



    if len(p.products.all()) ==1:
# для текстиля, для пленок 1 к-во - 1 место    	
		print(p.pack_number)
#действие
		total_pack = p.total
		product = p.products.first()
		product_quantity = product.quantity
		print(total_pack, product_quantity, p.point, total_pack/p.point, product.pack_product_id)
		raw_input("hello")
		if (p.total / p.point) < 150:
			print("можем делить к-во на мест")
			#проверка делиться ли нацело
			if product_quantity % p.point == 0:
			    print(product_quantity,"/",p.point,"=",product_quantity//p.point)
			    parcel_num = product_quantity//p.point
			    parcel_weight = p.weight/p.point
			    parcel_volume = p.volume/p.point
			    print(parcel_num, parcel_weight, parcel_volume)
			    raw_input("Тело цикла")
			    #разбиваем если все звезды сошлись
			    click_button_plus(p.pack_id, product.pack_product_id)
			    # a = "button[pack-id='{0}']".format(p.pack_id)
			    # button_plus=driver.find_element_by_css_selector(a)
			    # button_plus.click()
			    # b = "input[value='{0}']".format(product.pack_product_id)
			    # element = driver.find_element_by_css_selector(b)
			    # element.click()
			    inp_box = "input[name='pack[{0}][quantity][{1}]']".format(p.pack_id, product.pack_product_id)
			    element0 = driver.find_element_by_css_selector(inp_box)
			    element0.clear()
			    quant = str(parcel_num)
			    element0.send_keys(quant)
			    element000 = driver.find_element_by_css_selector("input[name='parcel_count_status']")
			    element000.click()
			    element111 = driver.find_element_by_css_selector("input#parcel-count")
			    element111.clear()
			    weight_push = str(parcel_weight)
			    volume_push = str(parcel_volume)
			    driver.find_element_by_css_selector("input#parcel-weight").send_keys(weight_push)
			    driver.find_element_by_css_selector("input#parcel-volume").send_keys(volume_push)
			    raw_input("Правильно? ")	

			    driver.find_element_by_class_name('parcel').click()
			    # ans = raw_input("Кликнулось? y/n ")
			    # if ans =='y':
			    # 	print("все норм кликнулось! )) ")

			    # else:
			    # 	print("Кликните вручную ")

			    #разбиваем если все звезды сошлись
			elif product_quantity % p.point != 0:
				print("Не делится нацело")
				raw_input("Не делится нацело")
				print(product_quantity,"// на цело",p.point,"=",product_quantity//p.point)
				main_parcel = product_quantity//p.point
				point_minus_one = p.point - 1
				parcel_weight = p.weight/p.point
				parcel_volume = p.volume/p.point
				#выбрать и нажать +
				click_button_plus(p.pack_id, product.pack_product_id)
				# a = "button[pack-id='{0}']".format(p.pack_id)
				# button_plus=driver.find_element_by_css_selector(a)
				# # WebDriverWait(driver, 10).until_not(EC.visibility_of_element_located((By.ID, "overley")))
				# button_plus.click()
				# #выбрать и нажать +
				# #вводим значение к-ва 
				# b = "input[value='{0}']".format(product.pack_product_id)
				# element = driver.find_element_by_css_selector(b)
				# element.click()
				#вводим значение к-ва 
				inp_box = "input[name='pack[{0}][quantity][{1}]']".format(p.pack_id, product.pack_product_id)
				element0 = driver.find_element_by_css_selector(inp_box)
				element0.clear()
				quant = str(parcel_num)
				element0.send_keys(quant)
				element000 = driver.find_element_by_css_selector("input[name='parcel_count_status']")
				element000.click()
				element111 = driver.find_element_by_css_selector("input#parcel-count")
				element111.clear()

				weight_push = str(parcel_weight)
				volume_push = str(parcel_volume)
				driver.find_element_by_css_selector("input#parcel-weight").send_keys(weight_push)
				driver.find_element_by_css_selector("input#parcel-volume").send_keys(volume_push)
				driver.find_element_by_class_name('parcel').click()

			else:
			    print("Не понятная хрень")
			    raw_input("Не понятная хрень")

			#проверка делиться ли нацело
		else:
			print("не можем делить т.к. цена свыше 150")
			""" Не проработана модель действий если нельзя поместить 1 посылка - 1 место
			"""
#действие

# для текстиля, для пленок 1 к-во - 1 место
    

    else:
		print("True", p.pack_number, p.products.all().first().name, len(p.products.all()))



#несколько мест, но 1 позиция наименования товара -  








# body = driver.find_element_by_tag_name('tbody')

# file_data = []
# body_rows = body.find_elements_by_tag_name('tr')
# for row in body_rows:
#     data = row.find_elements_by_tag_name('td')
#     file_row = []
#     for datum in data:
#         datum_text = datum.text.encode('utf8')
#         file_row.append(datum_text)
#     file_data.append(file_row)
# print()

#----------------------------------------------


























#Для ОДИНОЧНИКОВ---------------------------------------------------------------------------
#формируем выбор упаковочного
pack_num = input("Введите номер упаковочного: ")
print("Был выбран " + str(pack_num))
p = Pack.objects.get(pack_number=pack_num)
date=p.date_added.strftime('%d.%m.%Y')
client=Customer.objects.get(customer_id=p.customer_id)
client.external_id
weight = p.weight
zzz=ParcelPackProduct.objects.get(pack_id=p.pack_id)
plomba = Parcel.objects.get(parcel_id=zzz.parcel_id)

#--выбор упаковочного
driver.find_element_by_xpath("//input[@type='checkbox' and @value='" +str(x) + "']").click()
driver.find_element_by_xpath("//button[@class='btn btn-box-tool' and @pack-id='" +str(x) + "']").click()
#-----

#Заполняем данные для формирования посылки
Elem_weight=driver.find_element_by_name('parcel_weight').send_keys(str(p.weight))
Elem_volume=driver.find_element_by_name('parcel_volume').send_keys(str(p.volume))
driver.find_element_by_link_text('Сформировать посылку').click()

print("%s %s %s 1 %s" %(date, client, weight, plomba.external_id))
#-------------------------------------------------------------------------------------------




#для ОДНОЙ ПОЗИЦИИ И НЕСКОЛЬКО ПОСЫЛОК по равному к-ву
pack_num = input("Введите номер упаковочного: ")
print("Был выбран " + str(pack_num))
p = Pack.objects.get(pack_number=pack_num)
x = p.pack_id
date=p.date_added.strftime('%d.%m.%Y')
client=Customer.objects.get(customer_id=p.customer_id)
client.external_id
weight = p.weight
print("%s %s %s" %(date, client, weight))

#--выбор упаковочного
driver.find_element_by_xpath("//input[@type='checkbox' and @value='" +str(x) + "']").click()
driver.find_element_by_xpath("//button[@class='btn btn-box-tool' and @pack-id='" +str(x) + "']").click()
#-----

#выбор и ввод к-в
search = input("Какое к-во мне искать? ")
pack_quant = input("Введите по сколько штук упаковывать: ")
parcel_number = input("Введите на сколько посылок разбивать: ")

print("По: " + str(pack_quant) +" на:"+str(parcel_number)+" посылки")

#driver.find_element_by_name("pack['" +str(x) + "']")
driver.find_element_by_xpath("//input[@type='text' and @value='" +str(search) + "']").clear()
driver.find_element_by_xpath("//input[@type='text' and @value='" +str(search) + "']").send_keys(str(pack_quant))
#driver.find_element_by_xpath("//input[@type='checkbox' and @value='" +str(search) + "']").send_keys(str(pack_quant))

driver.find_element_by_name("parcel_count_status").click()
# driver.find_element_by_name("parcel_count").send_keys(Keys.LEFT)
# driver.find_element_by_id("parcel-count").send_keys(str(parcel_number))
#driver.find_element_by_name("parcel_count").send_keys(Keys.DELETE)
driver.find_element_by_name("parcel_count").send_keys(Keys.RIGHT)
driver.find_element_by_name("parcel_count").send_keys(Keys.BACK_SPACE)
raw_input('Введите на сколько посылок разбивать: & Press enter to continue: ')
#parcel=driver.find_element_by_id("parcel-count").clear()
#driver.find_element_by_id("parcel-count").send_keys(str(parcel_number))


#Заполняем данные для формирования посылки
w=round(p.weight/parcel_number, 2)
v=round(p.volume/parcel_number, 3)
driver.find_element_by_name('parcel_weight').clear()
driver.find_element_by_name('parcel_volume').clear()
driver.find_element_by_name('parcel_weight').send_keys(str(w))
driver.find_element_by_name('parcel_volume').send_keys(str(v))





driver.find_element_by_link_text('Сформировать посылку').click()
#-----------------------------------------------------------------------------



# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
# driver.execute_script("window.scrollTo(0, Y)") 
# driver.execute_script("window.scrollTo(0, 500)") центр экрана
# driver.execute_script("window.scrollTo(0, 1080)") самый низ экрана 
# where Y is the height (on a fullhd monitor it's 1080)






















#read familia in file

import xlrd, xlwt
import time
#----------------------------
#i=2
#----------------------------
rb = xlrd.open_workbook('/root/Yandex.Disk/самолеты/Санька/ФАМИЛИИ/1 000 000/10-я и 11-я(не залитая) 1000.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")

sheet1.write(0, 7, "Населенный пункт")
sheet1.write(0, 9, "Улица")
sheet1.write(0, 10, "Дом")
#----------------------------
#for rownum in range(3):
for rownum in range(305, 350):	
#----------------------------	
	row = sheet.row_values(rownum)
	print(row[0] + ' ' + row[1] +' '+row[2]+ ' '+ row[3] +'-first')

	linkElem=driver.find_element_by_name('lastName')
	linkElem1=driver.find_element_by_name('firstName')
	linkElem2=driver.find_element_by_name('middleName')
	buttonElem = driver.find_element_by_name('searchButton')

	linkElem.send_keys(row[0])
	linkElem1.send_keys(row[1])
	linkElem2.send_keys(row[2])

	buttonElem.click()
	time.sleep(5)
#result1 = driver.find_element_by_css_selector('td')
	try:
		result = driver.find_element_by_tag_name('tbody')
		a=unicode(result.text)
		z1=a.split('\n')

		for z000 in z1:
			if (row[3][6:10] + '-' +row[3][3:4])  in z000:
				search = z000
			else:
				search = 'Извините, таких абонентов в базе данных нет.'

		# for z000 in z1:
		# 	if row[3][6:10] in z000:
		# 		search = z000

		z2=search.split(' ')
		print(z2[5]); print(z2[6]); print(z2[-3])
		print('len = ', len(z2))
		#write in file
		sheet1.write(rownum, 7, z2[5])
		sheet1.write(rownum, 9, z2[6])
		sheet1.write(rownum, 10, z2[-3])

		#delete text on input
		linkElem=driver.find_element_by_name('lastName')
		linkElem1=driver.find_element_by_name('firstName')
		linkElem2=driver.find_element_by_name('middleName')
		buttonElem = driver.find_element_by_name('searchButton')
		linkElem.clear()
		linkElem1.clear()
		linkElem2.clear()
	except NoSuchElementException:
		print("Извините, таких абонентов в базе данных нет.")
		linkElem=driver.find_element_by_name('lastName')
		linkElem1=driver.find_element_by_name('firstName')
		linkElem2=driver.find_element_by_name('middleName')
		buttonElem = driver.find_element_by_name('searchButton')
		linkElem.clear()
		linkElem1.clear()
		linkElem2.clear()

book.save("/root/Yandex.Disk/самолеты/Санька/ФАМИЛИИ/1 000 000/little_help_me.xls")
