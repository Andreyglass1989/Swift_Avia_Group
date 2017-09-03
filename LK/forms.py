from django import forms
from django.forms import ModelForm
from login.models import User, UserProfile, ExpectedCargo
from LK.models import CustomerRecipients

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