# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.core.urlresolvers import reverse_lazy

from login.models import ManagerCustomerProfile, CustomerNovaPoshta, AirDataUploadFrom1C
from django.views.generic import ListView, CreateView
from LK.models import Customer, Pack, Zone

from django.contrib.auth.models import User

from ManagerAdmin.forms import ClientCreateForm
import requests, operator
# Create your views here.
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
import pandas as pd
from datetime import datetime 



entrepreneurs_dict = {'Варбанець Є.Р. ФОП': 26009054357407, 'СПД ЩАВИНСКАЯ НАТАЛИЯ РОМАНОВНА': 26003054348616, 'СПД ВАРБАНЕЦЬ ЛЮДМИЛА ПЕТРІВНА': 26007054340085, 'СПД САВЄЛЬЄВА ЛЮДМИЛА ПЕТРІВНА': 26009054358622, 'ЧОС М.В. ФОП': 26007054353395, 'Яковчук А.А. ФОП': 26004054347876}
entrepreneurs=pd.Series(entrepreneurs_dict)

id_priv_dict = {'Варбанець Є.Р. ФОП': '3a574ecf-a938-47fd-8034-bd9901aa85d6', 'СПД ЩАВИНСКАЯ НАТАЛИЯ РОМАНОВНА': 'f5886524-377a-42d1-9fa2-a5ced0de1d9c', 'СПД ВАРБАНЕЦЬ ЛЮДМИЛА ПЕТРІВНА': '68acdf17-321a-4585-8bc7-be7de2fcb163', 'СПД САВЄЛЬЄВА ЛЮДМИЛА ПЕТРІВНА': '0e80d3f5-fe09-4445-aa2d-06037cc41465', 'ЧОС М.В. ФОП': 'bccbaa87-adc3-489d-9420-b92747154471', 'Яковчук А.А. ФОП': '20edd1d5-3b9f-4492-9807-b3c5d8146e57'}
id_priv=pd.Series(id_priv_dict)

token_priv_dict = {'Варбанець Є.Р. ФОП': 'bT8WLCvBKMXAQFVoKyg3etRGMZ7P9pfqUsN6bGpNj6FeJt9LMP9OC3KXp/VRsldL+AKIENu6MatRnTMo0K2kGYY/hAWbZv+XlaKStCENu/3KvMzs4t0cwUdV8nZca250C6VLztndzF/u+2ZA0YVSnSssyvHgpQtxDTx8vQX0bDTmGGjjXvvPrMHlkqaI6xzNAtG+bNOijFKRHeY6mVThIt5L86hlwIFATqYAsmjSLPoyXW2cIi+iOS43sNX9oUSp0g==', 
'СПД ЩАВИНСКАЯ НАТАЛИЯ РОМАНОВНА': '23oaUCA/NIrAil3/X7u2do6v/KDxK2oFHsU0yBBPZf0Nlw143RdSp2p/jNmVksu4F9zigKFK5JLpMHiJINsCie2g2i3IcaDPmfU5iA1KGddSsygey6Lh/1lpTgDB4VhWuN0rPNNYDXf7yvH34ZGkA50Oi88dcU2vgNxdotp34KwqUsiR6pDYsp0a8vUt4p1oQr2mdCz5NXHPW1pnaTB2k/K4sE51fySHb7wSFNwxLcd8nwL80Fjtvf65C4XFuNM=', 
'СПД ВАРБАНЕЦЬ ЛЮДМИЛА ПЕТРІВНА': 'NP72msmkmglCvEdmm7iSZPCof1OgGcd/53DEPiLyHhMGZcDF0oYS7CJNwEXlW/ZA/Mh63VNQysp49drqlv1vUnhMPEwp3zYNmPep9o+GfnJrg/ZH/vB3Z/MSonqxd+QOBfaNyqS1IATcrSpJtmN0L4XuAFQ1R1gRBJK1uaX1VDKXxGK2S2vWPdmbFnPFXNbrcu3oll1+f5j8zoyVAXAlQVzfAKKiwHAnJx2JcC5RIW2yWmv4a/tXIJYMZOpEFtQ=', 
'СПД САВЄЛЬЄВА ЛЮДМИЛА ПЕТРІВНА': '4wglXzCEVbHjndC6jAPfI3zdYfkKNeso4k3dvSDtYp6INyb0vOKODVFeQgoWdfK2WuHGOBag3HbmW/Yo5pUhEueMA2xPCku84echQUOZ8WYhyLJAv3b+UTwaKM23c2gq1r7Z7cWIj70Yq1QakoVydWE8n3M2OuKtXPNwWVk41MxJdNBfcVgWInFfyPLS1hBAayG3YLqZvm9ybmjC7hz4KtFgl8ZKCzAGkY4iVmDnYN80JDoSEk+GbtfzD6217XyFwA==', 
'ЧОС М.В. ФОП': 'AGkeljWgYJ+9YSTFY0pbwkmxbmBigCJnjPEITKnJwEtnA46YnT2vPqzSTPtNXr2jp2byvv23F9T7kzzR03dHfCnZ5ShNPVYt9owX1eVMuC6Y0rNx81FgUm75MTphiycsbXcHkzJVXFe2kURf0lh08DOwMHkmPPZbInbRXXSNmt3ZcbxEiyr+oXsAyeptFtJJy8QDzYgMVyWpq7TTcCVlz26rG9y4HMN0aowMptCx+qZgO65bxclFozcwdEIFKlkqaQ==',
'Яковчук А.А. ФОП': 'bAw8Ng6RujV1wnpjSFzaiJl/2nm2yG94Zz8YdANno7fvJyLdtKMNf3Hv7nNvYsx67p9l5xSyfX6aq4YQVmq6JS+TLKogaQ+QAP4IUu2KLbBOXsWKyCq5KahRf9KmuN6kdgehGAHVUBKq6SmkqQs6RMV2DCOtSa5luQashjz8dvBSPj/RlUzTLw+58qzcAdhNRClfb4mURKhBlEBdckSLeCknFAt10Rue8KO5wbR3B7Ma9X/LW1o3ASHoSq7EyzY='}
token_priv = pd.Series(token_priv_dict)

dataALL = pd.DataFrame({'acc':entrepreneurs, 'id': id_priv, 'token': token_priv})






class ClientsListView(ListView):
	model = ManagerCustomerProfile
	template_name = 'clients.html'

	def get_context_data(self, **kwargs):
		context = super(ClientsListView, self).get_context_data(**kwargs)
		username = auth.get_user(self.request)
		table = ManagerCustomerProfile.objects.filter(manager_id=username.id)
		# customers = Customer.objects.filter()
		# print(dir(table))
		# user = UserProfile.objects.get(user_id=username.id)
		context={
			'username': username,
			'table': table
		}
		return context



# class ClientsCreateView(CreateView):
# 	model = Customer
# 	template_name = 'add-clients.html'
# 	success_url = '/ManagerAdmin/clients/'
# 	form_class = ClientForm



class NewPostListView(ListView):
	model = CustomerNovaPoshta
	template_name = 'NewPost.html'

	def get_context_data(self, **kwargs):
		context = super(NewPostListView, self).get_context_data(**kwargs)
		username = auth.get_user(self.request)
		table = CustomerNovaPoshta.objects.filter(customer__managercustomerprofile__manager_id=username.id)
		context={
			'username': username,
			'table': table
		}
		return context


class CargoListView(ListView):
	model = Pack
	template_name = 'CargoList.html'


	def get_context_data(self, **kwargs):
		context = super(CargoListView, self).get_context_data(**kwargs)
		username = auth.get_user(self.request)
		table = Pack.objects.filter(customer__managercustomerprofile__manager_id=username.id)
		context={
			'username': username,
			'table': table
		}
		return context


class ClientCreateView(CreateView):
    model = Customer
    template_name = "wizard-create-client.html"
    form_class = ClientCreateForm
    success_url =  reverse_lazy("ManagerAdmin:clients")


    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        print(context)
        print(form.errors)
        return self.render_to_response(context)


    def get_initial(self):
		self.initial = super(ClientCreateView, self).get_initial()
		username = self.request.user
		customer = Customer.objects.all()
		customer = customer.last()
		print(customer.customer_id)
		customer = 'SW0' + str(int(customer.customer_id)+1)
		self.initial['customer_number'] = customer
		print(self.initial)
		return self.initial


    def get_context_data(self, **kwargs):
		context = super(ClientCreateView, self).get_context_data(**kwargs)
		username = auth.get_user(self.request)
		print(username.id)
		choise = Zone.objects.all().order_by('name')
		customer = Customer.objects.all()
		customer = customer.last()
		print(customer.customer_id)
		customer = 'SW0' + str(int(customer.customer_id)+1)
		# self.initial['customer_number'] = customer
		print(customer)
		context={
			'choise': choise,
			'customer_number': customer,
		}
		return context


    def form_valid(self, form):
		response = super(ClientCreateView, self).form_valid(form)

#############
		# username = auth.get_user(self.request)
		# customer = Customer.objects.all()
		# customer = customer.last()
		# customer_plus_one = int(customer.customer_id)+1
		# usr = User.objects.get(id=username.id)
		# print(customer_plus_one, username.id) 
		# man_prof = ManagerCustomerProfile(manager=usr, customer=customer_plus_one)
		# man_prof.save()

#############
		# print(self.request.method)
		data = form.cleaned_data
		# print(data)
		# self.objects = form.save()
		# print(form)
		return super(ClientCreateView, self).form_valid(form)


       
	# def get_context_data(self, **kwargs):
	# 	context = super(ClientCreateView, self).get_context_data(**kwargs)
	# 	# username = auth.get_user(self.request)
	# 	choise = Zone.objects.all().order_by('name')
	# 	context={
	# 		'username': username,
	# 		'choice': choice,
	# 	}
	# 	return context




    # def form_valid(self, form):
    #     response = super(ClientsCreateView, self).form_valid(form)
    #     data = form.cleaned_data
    #     self.object = form.save()
        # d = data['name']+ data['lastname']
        # messages.success(self.request, "Клиент - %s %s, успешно добавлен!" % (data[u'lastname'].encode('utf8'), data[u'name'].encode('utf8')))
        #"Recipients - %s, was been success add!" % data['lastname']
#---SEND-MAIL--------------------------------------------------------------------------------------------
        # subject = 'Получатель добавлен'
        # message = "Получатель - %s %s, успешно добавлен!" % (data[u'lastname'].encode('utf8'), data[u'name'].encode('utf8'))
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [settings.EMAIL_HOST_USER, 'yak0b@rambler.ru']  # save_it.email,
        # #
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
#---SEND-MAIL--------------------------------------------------------------------------------------------
        # return super(ClientsCreateView, self).form_valid(form)


# class ClientsCreateView():
	

        # cargo_ne_obrabotan = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=1)
        # cargo_consol = Pack.objects.filter(customer_id=user.code_clienta,
        #                                    pack_status_id=2)  # user.code_clienta.pack_set.filter

        # cargo_consolidation = cargo_ne_obrabotan.count() + cargo_consol.count()
        # cargo_v_puti = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=5)
        # # ---- для вывода к-ва/цифры упаковочных на боковую панельку
        # cargo = Pack.objects.filter(customer_id = user.code_clienta, pack_status_id=8)





#  In [1]: %paste
# from login.models import ManagerCustomerProfile, CustomerNovaPoshta
# from django.views.generic import ListView, CreateView
# from LK.models import Customer

# ## -- End pasted text --

# In [2]: username=6

# In [3]: m=ManagerCustomerProfile.objects.filter(manager_id=username)

# In [4]: for n in m:                                             
#     cargo = Pack.objects.filter(customer_id = n.customer_id)
#    ...:     
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-4-fb18b50183f4> in <module>()
#       1 for n in m:
# ----> 2     cargo = Pack.objects.filter(customer_id = n.customer_id)
#       3 

# NameError: name 'Pack' is not defined

# In [5]: for LK.models import Pack
#   File "<ipython-input-5-17d20d271bc3>", line 1
#     for LK.models import Pack
#                        ^
# SyntaxError: invalid syntax


# In [6]: for LK.models imports Pack
#   File "<ipython-input-6-9ffc7dd93a6d>", line 1
#     for LK.models imports Pack
#                         ^
# SyntaxError: invalid syntax


# In [7]: from LK.models import Pack

# In [8]: for n in m:
#     cargo = Pack.objects.filter(customer_id = n.customer_id)
#    ...:     

# In [9]: cargo
# Out[9]: <QuerySet [<Pack: 130260679>, <Pack: 130260621>, <Pack: 130260616>, <Pack: 130260490>]>



def paymentCard(request):
    headers = {'id':'20edd1d5-3b9f-4492-9807-b3c5d8146e57', 'token':'bAw8Ng6RujV1wnpjSFzaiJl/2nm2yG94Zz8YdANno7fvJyLdtKMNf3Hv7nNvYsx67p9l5xSyfX6aq4YQVmq6JS+TLKogaQ+QAP4IUu2KLbBOXsWKyCq5KahRf9KmuN6kdgehGAHVUBKq6SmkqQs6RMV2DCOtSa5luQashjz8dvBSPj/RlUzTLw+58qzcAdhNRClfb4mURKhBlEBdckSLeCknFAt10Rue8KO5wbR3B7Ma9X/LW1o3ASHoSq7EyzY=', 'content-type': 'application/json' }
    url_today1 = 'https://acp.privatbank.ua/api/proxy/transactions/today?acc=26004054347876'
    url_last_day1 = 'https://acp.privatbank.ua/api/proxy/transactions/lastday?acc=26004054347876'
    z = requests.get('https://acp.privatbank.ua/api/proxy/transactions?acc=26004054347876&startDate=30-01-2019&endDate=20-02-2019', headers=headers)
    z3 = requests.get(url_today1, headers=headers)
    z4 = requests.get(url_last_day1, headers=headers)
    a = z3.json()
    b = z4.json()
    c = z.json()

    z1 = c['StatementsResponse']['statements']
    list = []
    for number in range(len(z1)):
        # print(number)
        obj = z1[number].values()[0]
        list.append(obj)
    list2 = sorted( list, key = operator.itemgetter('BPL_DAT_OD') )
    context = {
        "list": list2
    }
    return render(request, "payment.html", context)




url_B = 'https://acp.privatbank.ua/api/proxy/transactions/'
headers = {'id':'20edd1d5-3b9f-4492-9807-b3c5d8146e57', 'token':'bAw8Ng6RujV1wnpjSFzaiJl/2nm2yG94Zz8YdANno7fvJyLdtKMNf3Hv7nNvYsx67p9l5xSyfX6aq4YQVmq6JS+TLKogaQ+QAP4IUu2KLbBOXsWKyCq5KahRf9KmuN6kdgehGAHVUBKq6SmkqQs6RMV2DCOtSa5luQashjz8dvBSPj/RlUzTLw+58qzcAdhNRClfb4mURKhBlEBdckSLeCknFAt10Rue8KO5wbR3B7Ma9X/LW1o3ASHoSq7EyzY=', 'content-type': 'application/json' }

def repack_json_api(array):
    z1 = array['StatementsResponse']['statements']
    list = []
    for number in range(len(z1)):
        obj = z1[number].values()[0]
        list.append(obj)
    list2 = sorted( list, key = operator.itemgetter('BPL_DAT_OD') )
    return list2



def Today(request):
    query = request.GET.get("entrepreneurs")
    if query:
        print(query)

    url_last_day1 = 'https://acp.privatbank.ua/api/proxy/transactions/lastday?acc=26004054347876'
    z = requests.get(url_B + '?acc=26004054347876&startDate=30-01-2019&endDate=20-02-2019', headers=headers).json()
    # z3 = requests.get(url_today1, headers=headers)
    # z4 = requests.get(url_last_day1, headers=headers)
    # a = z3.json()
    # b = z4.json()
    list = repack_json_api(z)
    context = {
        "list": list
    }
    return render(request, "hello.html", context)


def todayPayment(request):
    query = request.GET.get("entrepreneurs")
    list = []
    if query:
        p = dataALL[dataALL.acc==int(query)]
        token0 = p.token
        id0 = p.id
        acc = p.acc
        print(token0.values[0], id0.values[0], acc.values[0])
        url_today = url_B + '/today?acc=' + str(acc.values[0])
        headers0 = {"id": id0.values[0], "token": token0.values[0], 'content-type': 'application/json'}
        z = requests.get(url_today, headers=headers0).json()
        list = repack_json_api(z)
        print(list)
    else:
        list = []
    context = {
        "list": list,
    }
    return render(request, "payment.html", context)


def lastdayPayment(request):
    # if request.is_ajax():
    query = request.GET.get("entrepreneurs")
    list = []

    if query:
        p = dataALL[dataALL.acc==int(query)]
        token0 = p.token
        id0 = p.id
        acc = p.acc
        # print(token0.values[0], id0.values[0], acc.values[0])
        # print(acc, token0, id0)
        url_lastday = url_B + '/lastday?acc=' + str(acc.values[0])
        print(url_lastday)
        headers0 = {"id": id0.values[0], "token": token0.values[0], 'content-type': 'application/json'}
        # print(headers0)
        z = requests.get(url_lastday, headers=headers0).json()
        list = repack_json_api(z)
        print(list)
        jsresp = JsonResponse({'list':list})
        return HttpResponse(jsresp.content, content_type='text/html')
    else:
        return render(request, "payment.html", {})
    # print(list)
            # context = {
            #     "list": list,
            # }
            # jsresp = JsonResponse(context)
            # return HttpResponse(jsresp.content, content_type='text/html')
    # else:
    #     list = []
    #     print(query)
    # url_lastday = url_B + '/lastday?acc=26004054347876'
    # z = requests.get(url_lastday, headers=headers).json()
    # list = repack_json_api(z)
    # context = {
    #     "list": list,
    # }
    # print(context)
    # return render(request, "payment.html", context)

def example_payment(request):
    # list_data = AirDataUploadFrom1C.objects.filter(air=324)
    query = request.GET.get("entrepreneurs")
    period1 = request.GET.get("period")
    period2 =request.GET.get("daterange")
    d_list = period2.split(" - ")
    datetime_object1 = datetime.strptime(d_list[0], '%m/%d/%Y')
    datetime_object2 = datetime.strptime(d_list[1], '%m/%d/%Y')

    p = dataALL[dataALL.acc==int(query)]
    token0 = p.token
    id0 = p.id
    acc = p.acc
    # print(token0.values[0], id0.values[0], acc.values[0])
    # url_today = url_B + str(period1) + '?acc=' + str(acc.values[0])
    url_period = url_B + '?acc=' + str(acc.values[0]) + '&startDate=' + datetime_object1.strftime("%d-%m-%Y") + '&endDate=' + datetime_object2.strftime("%d-%m-%Y")
    headers0 = {"id": id0.values[0], "token": token0.values[0], 'content-type': 'application/json'}
    # z = requests.get(url_today, headers=headers0).json()
    z1 = requests.get(url_period, headers=headers0).json()
    # list = repack_json_api(z)
    list1 = repack_json_api(z1)
    # currency = requests.get("https://acp.privatbank.ua/api/proxy/currency/", headers=headers0).json()
    # print(currency["USD"]["S"]["rate"], currency["USD"]["S"]["nbuRate"])

    # uan = requests.get("http://www.apilayer.net/api/live?access_key=9fb45c49256c9c1763f41585f4af1eeb").json()
    # print(uan['quotes']['USDCNY'])
    context = {
        "list": list1,
        # "list_data": list_data,
        # "USD1": currency["USD"]["S"]["rate"],
        # "USD_nbu": currency["USD"]["S"]["nbuRate"],
        # "CNY": uan['quotes']['USDCNY'],
        # "USD": uan['quotes']['USDUAH']
    }
    return render(request, "payment.html", context)