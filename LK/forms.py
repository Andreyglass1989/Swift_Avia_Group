# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, formset_factory, modelformset_factory, Textarea, TextInput
from login.models import User, UserProfile, Reviews, Buyout
from LK.models import CustomerRecipients, Pack, PackProduct
from django.core.validators import RegexValidator
from django.forms.models import inlineformset_factory
from djangoformsetjs.utils import formset_media_js





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
        model = Pack
        exclude = []



#MyFormSet = formset_factory(ExpectedCargoModelForm)

class ExpectedCargoPackModelForm(forms.ModelForm):
    class Meta:
        model = PackProduct
        exclude = ['weight_netto']

    class Media(object):
        js = formset_media_js + (
            # Other form media here
        )

PackProductFormSet = inlineformset_factory(Pack, PackProduct, extra=3,  exclude=['weight_netto', 'item_class_id', 'packed_quantity', 'volume'], can_delete=True, labels='Tovar', form=ExpectedCargoPackModelForm)

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


class BuyoutModelForm(forms.ModelForm):

    # comment = forms.CharField(widget=forms.Textarea(), help_text='Добавьте нужный комментарий к товару' required=False, error_messages={"required":"Поле не обязательно к заполнению"})


    class Meta:
        model = Buyout
        exclude = ['status', 'customer', 'amount_shipping']

        widgets = {
            'comment': Textarea(attrs={'cols': 25, 'rows': 1}),
            'price': TextInput(attrs={'size': '5'}),
            'quantity': TextInput(attrs={'size': '4'}),
            'size': TextInput(attrs={'size': '4'}),
            # 'customer': TextInput(attrs={'size': '1', 'max_length':'1'}),
            # 'name': TextInput(attrs={'size': '10'}),
            'color': TextInput(attrs={'size': '10'}),
        }




class BuyoutFormset(forms.ModelForm):

    class Meta:
        model = Buyout
        exclude = []

        labels = {
            'name': 'Наименование*',
        }

    class Media(object):
        js = formset_media_js + (
            # Other form media here
        )    


BuyoutFormSet = modelformset_factory(Buyout, extra=10,  can_delete=True, form=BuyoutFormset)