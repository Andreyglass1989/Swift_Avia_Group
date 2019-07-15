# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task

from login.models import CalculatorGroup
from django.core.mail import send_mail, EmailMessage
#from twilio.rest import Client
from django.conf import settings
#import datetime
from LK.models import (
    Pack, 
    Customer,
    )
from datetime import datetime, timedelta


@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="multiply_two_numbers")
def mul(x, y):
	number_1=x
	number_2 = y * random.randint(3, 100)
	total = number_1 * number_2
	new_obj = CalculatorGroup.objects.create(
		name="Celery and Redis forever!!! %s"%total,
		price = total,					
  		)
	return total

@task(name="hello_world")
def email():
    #clients_emails = ['yak0b@rambler.ru', '1989andreyglass@gmail.com']
    client_email = 'yak0b@rambler.ru'
    names_clients = []
    pochta = []
    telephone = []        
    cargo_consol = []
    date_time_now = datetime.datetime.now()
    day_today = date_time_now.strftime('%Y-%m-%d')
    subject = 'Swift Avia Group: Отчет по складу за {}'.format(date_time_now.strftime('%Y-%m-%d'))
    from_email = settings.EMAIL_HOST_USER
    to_list = [client_email]
#begin get Date
    
#end get Date
    customer_add_today = []
    cargo_consolidation = Pack.objects.filter(pack_status_id=2, date_added__icontains=day_today)
    cargo_zavedeno = Pack.objects.filter(pack_status_id=1, date_added__icontains=day_today)
    c_zavedeno = cargo_zavedeno.count() 


    c = cargo_consolidation.count()
    if c > 1:
        for car in cargo_consolidation:
            # print(car.customer)
            t=car.date_added
            t = t.replace(tzinfo=None)
            delta_time = date_time_now.replace(tzinfo=None) - t
            customer = Customer.objects.get(external_id=car.customer)
            customer_add_today.append(customer.external_id)
            if customer.email:
                pochta.append(customer.email)

            if customer.telephone:
                telephone.append(customer.telephone)

    elif c ==1:
        for car in cargo_consolidation:
            customer = Customer.objects.get(external_id=car.customer)
            customer_add_today.append(customer.external_id)
            if customer.email:
                pochta.append(customer.email)

            if customer.telephone:
                telephone.append(customer.telephone)
        #customer_add_today.append()
    else:
        customer_add_today.append("Nichego ne upakovano")
    
    c_z = 0 
    c=0      
    car_count = cargo_consolidation.count()
    for car in cargo_consolidation:
        c += car.weight
    for car in cargo_zavedeno:
        c_z += car.weight
		        
    message = 'Андрей, сегодня упаковано = {}kg, к-во упаковочных = {}; клиенты: {}'.format(c, car_count, customer_add_today) + str(pochta) + str(telephone)
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    return "message send to email succesfull!"

@task(name="otchet_zavedeno")
def email_zavedeno():
    #clients_emails = ['yak0b@rambler.ru', '1989andreyglass@gmail.com']
    client_email = 'yak0b@rambler.ru'
    pochta = []
    telephone = [] 
    cargo_consol = []
#begin get Date
    date_time_now = datetime.datetime.now()
    day_today = date_time_now.strftime('%Y-%m-%d')
    yesterday = datetime.now() + timedelta(days=-1)
    day_yesterday = yesterday.strftime('%Y-%m-%d')
#end get Date
    subject = 'Swift Avia Group: Отчет заведены упаковочные за {}'.format(date_time_now.strftime('%Y-%m-%d'))
    from_email = settings.EMAIL_HOST_USER
    to_list = [client_email]
    customer_add_today = []
    cargo_zavedeno = Pack.objects.filter(pack_status_id=1, date_added__icontains=day_today)
    c_zavedeno = cargo_zavedeno.count() 
   # c =  c_zavedeno.count()
    if c_zavedeno > 1:
        for car in  cargo_zavedeno:
            # print(car.customer)
            t=car.date_added
            t = t.replace(tzinfo=None)
            delta_time = date_time_now.replace(tzinfo=None) - t
            customer = Customer.objects.get(external_id=car.customer)
            customer_add_today.append(customer.external_id)
            if customer.email:
                pochta.append(customer.email)

            if customer.telephone:
                telephone.append(customer.telephone)

    elif c_zavedeno ==1:
        for car in cargo_zavedeno:
            customer = Customer.objects.get(external_id=car.customer)
            customer_add_today.append(customer.external_id)
            if customer.email:
                pochta.append(customer.email)

            if customer.telephone:
                telephone.append(customer.telephone)
        #customer_add_today.append()
    else:
        customer_add_today.append("Nichego ne upakovano")
    
    c_z = 0 
    c=0      
    for car in cargo_zavedeno:
        c_z += car.weight
                
    message ='Заведено = {} kg, к-во упаковочных = {}, клиенты: {}'.format(c_z, c_zavedeno, customer_add_today) + str(pochta) + str(telephone) 
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    return "message send to email succesfull!"







# @task(name="sum_list_numbers")
# def xsum():
#     yesterday = datetime.now() + timedelta(days=-1)
#     day_yesterday = yesterday.strftime('%Y-%m-%d')
#     #print(day_yesterday)

# #Date for mail
#     client_email = 'yak0b@rambler.ru'
#     subject = 'Ваш груз поступил к нам {}'.format(yesterday.strftime('%Y-%m-%d'))
#     from_email = settings.EMAIL_HOST_USER
#     to_list = [client_email]
# #Date for mail
#     customer_add_today = []
#     #cargo_consolidation = Pack.objects.filter(pack_status_id=2, date_added__icontains=day_yesterday)
#     cargo_consolidation0 = Pack.objects.filter(date_added__icontains=day_yesterday)
#     #cargo_consolidation1 = Pack.objects.filter(pack_status_id=1, date_added__icontains=day_yesterday)
#     #print(cargo_consolidation1.count())
#     #print(cargo_consolidation0.count())
#     #print(cargo_consolidation.count())
#     if cargo_consolidation0.count() != 0:
#         for car in cargo_consolidation0:
#             name = Customer.objects.get(external_id=car.customer)
#            # print(name.email)
#             subject = 'Ваш груз поступил к нам на склад'
#             message = u'Доброго времени суток, <strong>{}</strong>! \n<br/>Ваш груз (упаковочный номер {}) успешно поступил на наш склад. \n<br/>Подробную информацию можно посмотреть в личном кабинете нашего сайта. \n<br/>Если у Вас возникли вопросы, пожалуйста свяжитесь с Вашим менеджером любым удобным для Вас способом (Ваш код клиента: <strong>{}</strong>). \n<br/>Спасибо, что выбрали нашу компанию! <br/><p style="color: red; size:10">Отвечать на это письмо не нужно, оно создано автоматически. Получатель: {}</p>'.format(name.firstname, car.pack_number, car.customer, name.email)
#             from_email = settings.EMAIL_HOST_USER
#             #to_list = [client_email]
#             send_mail(subject, message, from_email, to_list, fail_silently=True)
#    	return "message send to email succesfull!"




# @task(name="send-sms")
# def send_sms():
# 	# Your Account SID from twilio.com/console
# 	account_sid = "AC9014a034cc401571a651f3c0144416b2"
# 	# Your Auth Token from twilio.com/console
# 	auth_token  = "5d99208d221c2421d41bf84d0df846e2"
# 	client = Client(account_sid, auth_token)
# 	message = client.messages.create(
# 		to=("+380937190220"),
# 		from_="+14153606834",
# 		body="Hello from Python!")
# 	return "Sms succesfull send!"


@task()
def xsum2(numbers):
    return sum(numbers)