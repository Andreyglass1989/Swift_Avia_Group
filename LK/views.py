# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_protect
from django.http import Http404
from django.contrib import auth
from login.models import UserProfile, Reviews
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
#CBV-----------------
# from django.views.generic import DetailView
# from django.views.generic import ListView
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
#CBV------------------

from LK.forms import UserModelForm, RecipientsModelForm, ExpectedCargoModelForm, ExpectedCargoPackModelForm, EmailForm, ReviewsForm, PackProductFormSet

from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template import Context
from django.template.loader import get_template

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#
from LK.models import Pack, PackProduct, CustomerRecipients, Country
from login.models import CalculatorGroup

from django.db.models.base import ObjectDoesNotExist
from django.db import transaction
# Create your views here.

User = get_user_model()

#-------------------------------------------------------Menu----------------------------------------#
def index(request):
    user = auth.get_user(request)
    try:
        user0 = UserProfile.objects.get(user_id=user.id)
    except ObjectDoesNotExist:
        user0 = None

    pack = Pack.objects.all()
    query = request.GET.get("query")
    pack_list = None
    if query:
        pack_list = pack.filter(pack_number__icontains=query)
    context = {
            'username': auth.get_user(request).username,
            'user': user,
            'pack_list': pack_list,
            'user0': user0,
        }
    return render(request, 'main.html', context)

def about_us(request):
    user = auth.get_user(request)
    try:
        user0 = UserProfile.objects.get(user_id=user.id)
    except ObjectDoesNotExist:
        user0 = None

    context = {'username': user.username,
               'user0': user0,
               }
    return render(request, 'about_us.html', context)


def partner(request):
    user = auth.get_user(request)
    try:
        user0 = UserProfile.objects.get(user_id=user.id)
    except ObjectDoesNotExist:
        user0 = None

    context = {'username': user.username,
               'user0': user0,
               }
    return render(request, 'partner.html', context)



@csrf_protect
def contacts(request):
    user = auth.get_user(request)
    try:
        user0 = UserProfile.objects.get(user_id=user.id)
    except ObjectDoesNotExist:
        user0 = None

    form_email = EmailForm
    # new logic!
    if request.method == 'POST':
        form = form_email(data=request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            cont_email = request.POST.get('email', '')
            tema = request.POST.get('tema', '')
            msg = request.POST.get('message', '')
            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
        context = Context({
            'contact_name': name,
            'contact_email': cont_email,
            'tema': tema,
            'form_content': msg,

        })
        content = template.render(context)

        subject = tema
        message = msg
        from_email = str(cont_email)
        from_email0 = [from_email]
        # print(from_email)
        # print (type(from_email))
        to_list = [settings.EMAIL_HOST_USER]
        # print (settings.EMAIL_HOST_USER)
        # print (type(settings.EMAIL_HOST_USER))
        send_mail(subject, message, from_email0, to_list, fail_silently=True)
        return HttpResponseRedirect("/contacts/")
    return render(request, 'contacts.html', {'form': form_email, 'username': auth.get_user(request).username, 'user0':user0,})


    #
    # context = {'username': auth.get_user(request).username,
    #            'email': email,
    #            }
    # return render(request, 'contacts.html', context)

#--------------SEND MAIL TO US ---------------------------
# @csrf_protect
# def send_mail_to_us(request):
#
#     if request.method == 'GET':
#         print("get data")
#     if request.method == 'POST':
#         print("post data")
#         print(request.POST)
#         name = request.POST.get("name")
#         print(name)
#         email = request.POST.get("email")
#         print(email)
#         tema = request.POST.get("tema")
#         print(tema)
#         msg = request.POST.get("message")
#         print(msg)
#         #---from backend send mail-----
#         subject = tema
#         message = msg
#         from_email = email
#         to_list = settings.EMAIL_HOST_USER
#         print(to_list)
#
#         send_mail(subject, message, from_email, to_list, fail_silently=True)
#         return HttpResponseRedirect("/contacts/")
#     template_name = "main.html"
#     context = {}
#     return render(request, template_name, context)
#--------------END SEND MAIL TO US ---------------------------



def if_delivery(request):
    user = auth.get_user(request)
    try:
        user0 = UserProfile.objects.get(user_id=user.id)
    except ObjectDoesNotExist:
        user0 = None

    otziv = Reviews.objects.all().order_by('-date_add')
    #username = auth.get_user(request).first_name
    context = {'user0': user0,
               'otziv': otziv[:3],
               'username': user.username,
               }
    return render(request, 'if_delivery.html', context)


def service(request):
    user = auth.get_user(request)
    try:
        user0 = UserProfile.objects.get(user_id=user.id)
    except ObjectDoesNotExist:
        user0 = None

    calculator = CalculatorGroup.objects.all().order_by('name')    
    context = {'user0': user0,
               'username': user.username,
               'calculator': calculator,
               }
    return render(request, 'service.html', context)
    


def all_cargo(request):
    #username = auth.get_user(request)
    #user = UserProfile.objects.get(user_id=username.id)
    cargo_ne_obrabotan = Pack.objects.filter( pack_status_id=1)
    clients_emails = []
    names_clients = []
    # if cargo_ne_obrabotan:
    #     for cargo in cargo_ne_obrabotan:
    #         if cargo.customer is not None:
    #             print(cargo.customer)
            # clients_emails = username.email
            # name_client = username.first_name
            # for gr in cargo_consolidation:
            #     print(gr.pack_number)
            #     gruz0 = gr.pack_number
            #     # print(gruz.pack_number)
            #     gruz.append(int(gr.pack_number))
            # print('i-%s' % gruz)
            # print(client_email)
            # print('%s' % name_client)
            # if cargo_consolidation:
            #     # send mail(subject, message, from_email, to_list, fail_silently=True)
            #     subject = 'Swift Avia Group: Ваш груз поступил к нам на склад'
            #     message = 'Доброго времени суток, уважаемый клиент %s! Ваш груз %s(подробности в личном кабинете) успешно обработан нашим складом и он попадет на ближайший вылет. Спасибо, что выбрали нашу компанию!' % (name_client.encode('utf8'), gruz)
            #     from_email = settings.EMAIL_HOST_USER
            #     to_list = [client_email, settings.EMAIL_HOST_USER]
            #
            #     send_mail(subject, message, from_email, to_list, fail_silently=True)
            #     # ------end--------send mail------------------------------------

    cargo_consolidation = Pack.objects.filter( pack_status_id=2)
    # for cargo in cargo_consolidation:
    #     print(cargo.customer)
    context = {'username': auth.get_user(request).username,
               'cargo_consolidation': cargo_consolidation,
               'cargo_ne_obrabotan': cargo_ne_obrabotan,
               }
    return render(request, 'all_cargo.html', context)


def lk (request):
    username = auth.get_user(request)
    # ---- для вывода к-ва/цифры упаковочных на боковую панельку
    user = UserProfile.objects.get(user_id=username.id)
    cargo_ne_obrabotan = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=1)
    cargo_consol = Pack.objects.filter(customer_id=user.code_clienta,
                                       pack_status_id=2)  # user.code_clienta.pack_set.filter
    cargo_consolidation = cargo_ne_obrabotan.count() + cargo_consol.count()
    cargo_v_puti = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=5)
    # ---- для вывода к-ва/цифры упаковочных на боковую панельку
    if username:
        try:
            user = UserProfile.objects.get(user_id=username.id)
        except UserProfile.DoesNotExist:
            user = None
        context = {
                'username': username,
                'user': user,
            # ---- для вывода к-ва/цифры упаковочных на боковую панельку
              #  'cargo_ne_obrabotan': cargo_ne_obrabotan,
                'cargo_consolidation': cargo_consolidation,
                'cargo_v_puti': cargo_v_puti,

            # ---- для вывода к-ва/цифры упаковочных на боковую панельку
            }
    return render(request, 'LK.html', context)


#-------------------------------------------------------Menu----------------------------------------#

def about_user(request):
    username = auth.get_user(request)
    user = UserProfile.objects.get(user_id = username.id)
    cargo_ne_obrabotan = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=1)
    cargo_consol = Pack.objects.filter(customer_id=user.code_clienta,
                                       pack_status_id=2)  # user.code_clienta.pack_set.filter
    cargo_consolidation = cargo_ne_obrabotan.count() + cargo_consol.count()
    cargo_v_puti = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=5)
    # ---- для вывода к-ва/цифры упаковочных на боковую панельку


    if request.method == "POST":
        form = ReviewsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Благодарим за отзыв!!!")
            return redirect("/LK/about_user/")
    else:
        form = ReviewsForm(initial={'reviews_client': user.code_clienta, 'recomend': True})

    context = {
        'username': username,
        'user': user,
        'cargo_v_puti': cargo_v_puti,
        'cargo_consolidation': cargo_consolidation,
        'form': form,
    }
    return render(request, 'about_user.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = "edit.html"
    form_class = UserModelForm
    success_url = '/LK/about_user/'

    def form_valid(self, form):
        response = super(UserUpdateView, self).form_valid(form)
        messages.success(self.request, "Данные успешно сохранены!!!")
        return response


def consolidation(request):
    username = auth.get_user(request)
    user = UserProfile.objects.get(user_id=username.id)
    cargo_ne_obrabotan = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=1)
    cargo_consol = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=2)            #user.code_clienta.pack_set.filter
    cargo_v_puti = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=5)
    cargo_consolidation = cargo_ne_obrabotan.count()+cargo_consol.count()

    client_email = username.email
    name_client = username.first_name
    # gruz=[]
    # for gr in cargo_consolidation:
    #     print(gr.pack_number)
    #     gruz0 = gr.pack_number
    #     #print(gruz.pack_number)
    #     gruz.append(int(gr.pack_number))
    # print(client_email)
    # print('%s' % name_client)
    # if cargo_consolidation:
    #     # send mail(subject, message, from_email, to_list, fail_silently=True)
    #     subject = 'Swift Avia Group: Ваш груз поступил к нам на склад'
    #     message = 'Доброго времени суток, уважаемый клиент %s! Ваш груз %s(подробности в личном кабинете) успешно обработан нашим складом и он попадет на ближайший вылет. Спасибо, что выбрали нашу компанию!' % (name_client.encode('utf8'), gruz)
    #     from_email = settings.EMAIL_HOST_USER
    #     to_list = [client_email, settings.EMAIL_HOST_USER]
    #
    #     send_mail(subject, message, from_email, to_list, fail_silently=True)
    #     # ------end--------send mail------------------------------------

    context = {
        'username': username,
        'user': user,
        'cargo_consol': cargo_consol,
        'cargo_ne_obrabotan': cargo_ne_obrabotan,
        'cargo_v_puti': cargo_v_puti,
        'cargo_consolidation': cargo_consolidation,
    }
    return render(request, 'consolidation.html', context)


def v_puti(request):
    username = auth.get_user(request)
    user = UserProfile.objects.get(user_id=username.id)
    cargo = user.code_clienta.pack_set.filter(customer_id=user.code_clienta, pack_status_id=5).order_by('-date_added')#Pack.objects.filter
    cargo_v_puti = cargo
    cargo_ne_obrabotan = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=1)
    cargo_consol = Pack.objects.filter(customer_id=user.code_clienta,
                                       pack_status_id=2)  # user.code_clienta.pack_set.filter

    cargo_consolidation = cargo_ne_obrabotan.count() + cargo_consol.count()
    context = {
        'username': username,
        'user': user,
        'cargo': cargo,
        'cargo_v_puti': cargo_v_puti,
        'cargo_consolidation': cargo_consolidation,
    }
    return render(request, 'v_puti.html', context)

def priletel(request):
    username = auth.get_user(request)
    user = UserProfile.objects.get(user_id=username.id)
    cargo_ne_obrabotan = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=1)
    cargo_consol = Pack.objects.filter(customer_id=user.code_clienta,
                                       pack_status_id=2)  # user.code_clienta.pack_set.filter
    cargo_consolidation = cargo_ne_obrabotan.count() + cargo_consol.count()
    cargo_v_puti = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=5)
    # ---- для вывода к-ва/цифры упаковочных на боковую панельку
    # cargo = Pack.objects.filter(customer_id = user.code_clienta, pack_status_id = 7, date_added__year = '2017').order_by('-date_added')
    cargo = user.code_clienta.pack_set.filter(customer_id = user.code_clienta, pack_status_id = 7, date_added__year = '2017').order_by('-date_added')

    paginator = Paginator(cargo, 15)  # Show 1 contacts per page Paginator begin
    page = request.GET.get('page')
    try:
        cargo = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cargo = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cargo = paginator.page(paginator.num_pages)  # """"""Paginator end"""""

    #
    # for car in cargo:
    #     tovar = car.packproduct_set.all()
    #     print (tovar)
    context = {
        'username': username,
        'user': user,
        'cargo_consolidation': cargo_consolidation,
        'cargo_v_puti': cargo_v_puti,
        'cargo': cargo,
    }
    return render(request, 'priletel.html', context)


#
# class DetailDetailView(DetailView):
#     template_name = 'priletel.html'
#
#     def get_object(self):
#         username = self.kwargs.get("username")
#         print(self.kwargs)
#         if username is None:
#             raise Http404
#         return get_object_or_404(User, username__iexact=username)






def detail (request, pack_number):
    username = auth.get_user(request)
    user = UserProfile.objects.get(user_id=username.id)
    packid = Pack.objects.get(pack_number = pack_number)
    cargo = PackProduct.objects.filter(pack_id = packid.pack_id)
    context = {
        'username': username,
        'user': user,
        'cargo': cargo,
        'pack_number': pack_number,
    }
    return render(request, 'detail_v_puti.html', context)


#--------------------------------------------------------------------------------------------
def recipients (request):
    username = auth.get_user(request)
    user = UserProfile.objects.get(user_id=username.id)
    cargo_ne_obrabotan = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=1)
    cargo_consol = Pack.objects.filter(customer_id=user.code_clienta,
                                       pack_status_id=2)  # user.code_clienta.pack_set.filter
    cargo_consolidation = cargo_ne_obrabotan.count() + cargo_consol.count()
    cargo_v_puti = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=5)
    # ---- для вывода к-ва/цифры упаковочных на боковую панельку
    recip = CustomerRecipients.objects.filter(customer_id = user.code_clienta)
    context = {
        'username': username,
        'user': user,
        'cargo_consolidation': cargo_consolidation,
        'cargo_v_puti': cargo_v_puti,
        'recip': recip,
    }
    return render(request, 'recipients.html', context)



class RecipientsCreateView(CreateView):
    model = CustomerRecipients
    template_name = "add_recipients.html"
    form_class = RecipientsModelForm
    success_url = "/LK/recipients/"

    def form_valid(self, form):
        response = super(RecipientsCreateView, self).form_valid(form)
        data = form.cleaned_data
        self.object = form.save()
        # d = data['name']+ data['lastname']
        messages.success(self.request, "Получатель - %s %s, успешно добавлен!" % (data[u'lastname'].encode('utf8'), data[u'name'].encode('utf8')))
        #"Recipients - %s, was been success add!" % data['lastname']
#---SEND-MAIL--------------------------------------------------------------------------------------------
        # subject = 'Получатель добавлен'
        # message = "Получатель - %s %s, успешно добавлен!" % (data[u'lastname'].encode('utf8'), data[u'name'].encode('utf8'))
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [settings.EMAIL_HOST_USER, 'yak0b@rambler.ru']  # save_it.email,
        # #
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
#---SEND-MAIL--------------------------------------------------------------------------------------------
        return super(RecipientsCreateView, self).form_valid(form)

    def get_initial(self):
        initial = super(RecipientsCreateView, self).get_initial()
        username = self.request.user
        email_clienta = username.email
        user = UserProfile.objects.get(user_id = username.id)
        self.initial = {'customer': user.code_clienta,
                        'email':email_clienta,
                        }
        return self.initial

    # def get_context_data(self, **kwargs):
    #     context = super(RecipientsCreateView, self).get_context_data(**kwargs)
    #     context = {
    #         'title': 'получателя'
    #     }
    #     return context

class RecipientsUpdateView(UpdateView):
    model = CustomerRecipients
    template_name = "edit_recipients.html"
    form_class = RecipientsModelForm
    success_url = "/LK/recipients/"

    def form_valid(self, form):
        response = super(RecipientsUpdateView, self).form_valid(form)
        self.object = form.save()
        messages.success(self.request, "Изменения успешно сохранены!")

        return super(RecipientsUpdateView, self).form_valid(form)


# class RecipientsDeleteView(DeleteView):
#     model = CustomerRecipients
#     template_name = "remove.html"
#     success_url = reverse_lazy('recipients')#"/LK/recipients/"
#
#     def get_context_data(self, **kwargs):
#         context = super(RecipientsDeleteView, self).get_context_data(**kwargs)
#         #recip = self.get_object()
#         #context['title'] = recip.lastname + ' ' + recip.name
#         return context
#
#     def delete(self, request, *args, **kwargs):
#         response = super(RecipientsDeleteView, self).delete(request, *args, **kwargs)
#         recip = self.get_object()
#         #success_url = self.get_success_url()
#         self.object.delete()
#         messages.success(self.request, "Получатель %s был удален!" %recip.name)
#         return super(RecipientsDeleteView, self).delete(request, *args, **kwargs) #HttpResponseRedirect(success_url)


def remove_recip(request, pk):
    recip = CustomerRecipients.objects.get(cr_id=pk)
    if request.method == "POST":
        recip.delete()
        r = recip.lastname + ' ' + recip.name
        messages.success(request, u"Получатель %s был удален." % r)
        return redirect("/LK/recipients/")
    else:
        #recip = u'Recip ' + recip.lastname + ' ' + recip.name
        form = RecipientsModelForm(instance=recip)
        rec = u'Получатель ' + recip.lastname + ' ' + recip.name
    return render(request, 'remove.html', {'title': rec})

#-----------------------------------------------------------------------------------

def oplata(request):
    weight_full = 0
    username = auth.get_user(request)
    user = UserProfile.objects.get(user_id=username.id)
    cargo = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=5).order_by('-date_added')
    for car in cargo:
        weight_full = weight_full + car.weight
    oplata = weight_full * user.stavka
    context = {
        'username': username,
        'user': user,
        'cargo': cargo,
        'weight_full': weight_full,
        'oplata': oplata,

    }
    return render(request, 'oplata.html', context)

#--------------------------------------ExpectedCargo-----------------------------------
class ExpectedCargoListView(ListView):
    model = Pack
    template_name = "expected_cargo.html"
    #paginate_by = 6
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super(ExpectedCargoListView, self).get_context_data(**kwargs)
        username = auth.get_user(self.request)
        user = UserProfile.objects.get(user_id=username.id)
        cargo_ne_obrabotan = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=1)
        cargo_consol = Pack.objects.filter(customer_id=user.code_clienta,
                                           pack_status_id=2)  # user.code_clienta.pack_set.filter

        cargo_consolidation = cargo_ne_obrabotan.count() + cargo_consol.count()
        cargo_v_puti = Pack.objects.filter(customer_id=user.code_clienta, pack_status_id=5)
        # ---- для вывода к-ва/цифры упаковочных на боковую панельку
        cargo = Pack.objects.filter(customer_id = user.code_clienta, pack_status_id=8)
        context = {
            'username': username,
            'user': user,
            'cargo': cargo,
            'cargo_consolidation': cargo_consolidation,
            'cargo_v_puti': cargo_v_puti,
        }

        return context




class ExpectedCargoCreateView(CreateView):
    model = Pack
    template_name = "add_excepted_cargo.html"
    form_class = ExpectedCargoModelForm
    success_url = "/LK/excepted_cargo/"

    # def form_valid(self, form):
    #     response = super(ExpectedCargoCreateView, self).form_valid(form)
    #     data = form.cleaned_data
    #     self.object = form.save()
    #     # d = data['name']+ data['lastname']
    #     messages.success(self.request, "Груз - успешно добавлен в <ОЖИДАЕМЫЕ>!" )
    #     return super(ExpectedCargoCreateView, self).form_valid(form)

    def get_initial(self):
        initial = super(ExpectedCargoCreateView, self).get_initial()
        username = self.request.user
        user = UserProfile.objects.get(user_id=username.id)
        pack = Pack.objects.all()
        #pack = pack.count() + 191100000
        #print(dir(pack))
        pack = pack.first()
        pack = int(pack.pack_number) + 1
        self.initial = {'customer': user.code_clienta,
                        'pack_status': 8,
                        'sklad': 1,
                        'packlist': 0,
                        'def_field': 0,
                        'sandbox': 0,
                        'currency': 2,
                        'currency_code': 'USD',
                        'currency_value': 1,
                        'total': 1.0,
                        'volume': 1.0,
                        'language': 2,
                        'pack_number': pack,
                        }
        return self.initial



    def get_context_data(self, **kwargs):
        data = super(ExpectedCargoCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['pack_form'] = PackProductFormSet(self.request.POST)
            print(data['pack_form'])
        else:
            data['pack_form'] = PackProductFormSet()
            print(data['pack_form'])
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pack_form = context['pack_form']
        with transaction.atomic():
            self.object = form.save()

            if pack_form.is_valid():
                pack_form.instance = self.object
                pack_form.save()
                messages.success(self.request, "Груз - успешно добавлен в <ОЖИДАЕМЫЕ>!")
        return super(ExpectedCargoCreateView, self).form_valid(form)




    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     pack_form = context['pack_form']
    #     with transaction.atomic():
    #         form.instance.created_by = self.request.user
    #         form.instance.updated_by = self.request.user
    #         self.object = form.save()
    #     if pack_form.is_valid():
    #         pack_form.instance = self.object
    #         pack_form.save()
    #         messages.success(self.request, "Груз - успешно добавлен в <ОЖИДАЕМЫЕ>!")
    #     return super(ExpectedCargoCreateView, self).form_valid(form)





    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     pack_form = PackProductFormSet()
    #     return self.render_to_response(self.get_context_data(form=form,
    #                                                          pack_form=pack_form))
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     pack_form = PackProductFormSet(self.request.POST)#, self.request.FILES)
    #     if (form.is_valid() and pack_form.is_valid()):
    #         return self.form_valid(form, pack_form)
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form, pack_form=pack_form))
    #
    #
    # def form_valid(self, form, pack_form):
    #     form.instance.user = self.request.user
    #     self.object = form.save()
    #     pack_form.instance = self.object
    #     pack_form.save()
    #     messages.success(self.request, "Груз - успешно добавлен в <ОЖИДАЕМЫЕ>!")
    #     return HttpResponseRedirect(self.get_success_url())



class ExpectedCargoUpdateView(UpdateView):
    model = Pack
    template_name = "edit_expected_cargo.html"
    form_class = ExpectedCargoModelForm
    success_url = "/LK/excepted_cargo/"


    def get_context_data(self, **kwargs):
        data = super(ExpectedCargoUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['pack_form'] = PackProductFormSet(self.request.POST, instance=self.object)
        else:
            data['pack_form'] = PackProductFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pack_form = context['pack_form']
        with transaction.atomic():
            self.object = form.save()

            if pack_form.is_valid():
                pack_form.instance = self.object
                pack_form.save()
                messages.success(self.request, "Изменения успешно сохранены!")
            else:
                pack_form = context['pack_form']
                messages.error(self.request, "Ooops! Заполните *обязательные поля для наименований товара!")    
        return super(ExpectedCargoUpdateView, self).form_valid(form)



def remove_excepted_cargo(request, pk):
    excepted_cargo = Pack.objects.get(pack_id=pk)
    if request.method == "POST":
        r = u'уп - %s, %s кг' %(excepted_cargo.pack_number, excepted_cargo.weight)
        excepted_cargo.delete()
        messages.success(request, u"Груз %s был удален." % r)
        return redirect("/LK/excepted_cargo/")
    else:
        # recip = u'Recip ' + recip.lastname + ' ' + recip.name
        form = ExpectedCargoModelForm(instance=excepted_cargo)
        rec = u'Груз уп - %s, %s кг' %(excepted_cargo.pack_number, excepted_cargo.weight)
    return render(request, 'remove.html', {'title': rec})

#-----------------------------------END---ExpectedCargo-----------------------------------


#-------------Служебные функции-------------------------------------------------------------------
#def info_about_cargo():

# def search (request):
#     if request.method == "POST":
#         search_text = request.POST['search_text']
#         if search_text > '':
#             pack_res = Pack.objects.filter(pack_number__contains=search_text)
#         else:
#             pack_res = Pack.objects.none()
#             text = 1
#     else:
#         search_text = ''
#     print(pack_res)
#     return render('search.html', {'pack_res': pack_res})


def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("MyModel")

    row_num = 0

    columns = [
        (u"ID", 2000),
        (u"Title", 6000),
        (u"Description", 8000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in queryset:
        row_num += 1
        row = [
            obj.pk,
            obj.title,
            obj.description,
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


export_xls.short_description = u"Export XLS"





#-------------Служебные функции-------------------------------------------------------------------
