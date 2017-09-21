# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from login.models import User, UserProfile, ExpectedCargo, Reviews
from LK.models import CustomerRecipients
from django.core.validators import RegexValidator



class RecipientsModelForm(forms.ModelForm):
    class Meta:
        model = CustomerRecipients
        fields = ['name', 'lastname', 'phone', 'city', 'street', 'home', 'room', 'customer', 'country']



class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'email']
        exclude = ['username', 'date_joined', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'password']


class ExpectedCargoModelForm(forms.ModelForm):
    class Meta:
        model = ExpectedCargo
        fields = ['name', 'quantity',  'price', 'post_delivery', 'treck', 'comment', 'url', 'customer']



class EmailForm(forms.Form):
    name    = forms.CharField(widget=forms.TextInput(attrs={'placeholder': u"Ваше имя:"}), required=True)
    email   = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': u"Ваша почта:"}), required=True)
    tema    = forms.CharField(widget=forms.TextInput(attrs={'placeholder': u"Тема:"}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': u"Сообщение"}))

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.fields['contact_name'].label = "Your name:"
    #     self.fields['contact_email'].label = "Your email:"
    #     self.fields['content'].label = "What do you want to say?"

class ReviewsForm(forms.ModelForm):
    class Meta():
        model = Reviews
        fields = ['text_reviews', 'recomend', 'reviews_client']

    text_reviews    = forms.CharField(widget=forms.Textarea(attrs={'placeholder': u"Добавьте отзыв"}), required=True)

