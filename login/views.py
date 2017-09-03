# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from login.forms import RegistrationForm
from django.views.generic.edit import FormView

# Create your views here.
@csrf_protect
def login (request):
    args = {}
    #args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Пользователь не найден!")
            #args['login_error'] = "Пользователь не найден!"
            return render(request, "login.html", args)
    else:
        return render(request, "login.html", args)

def logout (request):
    auth.logout(request)
    return  redirect('/')


@csrf_protect
def register (request):
    args={}
    args['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            messages.error(request, "Вам не присвоен код клиента! и не заполнены дополнительные данные, свяжитесь с вашим менеджером, указав свой логин, для пользования Личным Кабинетом")
            return redirect("/")                                           # room:add_character
        else:
            args['form'] = new_user_form
            messages.error(request, "Ooops! Что-то пошло не так!")
    return  render(request, "register.html", args)



     # #send mail(subject, message, from_email, to_list, fail_silently=True)
     #  subject = 'Recovery password'
     #  message = 'Hello man! '
     #  from_email = settings.EMAIL_HOST_USER
     #  to_list =  [save_it.email, settings.EMAIL_HOST_USER]
     #
     #  send_mail(subject,message,from_email,to_list,fail_silently=True)


# class RegistrationForm(FormView):
#     form_class = RegistrationForm
#     success_url = "/"
#     template_name = "login/reg_form.html"
#
#     def form_valid(self, form):
#         form.save()
#         return super(RegistrationForm, self).form_valid(form)

