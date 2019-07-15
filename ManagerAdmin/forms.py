from django import forms
from django.forms import ModelForm, formset_factory, modelformset_factory, Textarea, TextInput
from login.models import User, UserProfile, Reviews, CalculatorGroup, Buyout
from LK.models import Customer
from django.core.validators import RegexValidator
# from django.forms.models import inlineformset_factory
# from djangoformsetjs.utils import formset_media_js


class ClientCreateForm(forms.ModelForm):

	class Meta:
		model = Customer
		exclude = ['status', 'address_id', 'store_id', 
				   'color', 'typ', 'safe', 'sandbox', 
				   'newsletter', 'partner_id', 'approved',
				   'customer_group_id', 'customer_number']
