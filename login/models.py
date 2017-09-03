# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from LK.models import Customer
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    adress = models.CharField(max_length=100, default=None)
    phone = models.CharField(max_length=15)
    GANDER_CHOISE =(
		('Male', 'M'),
		('Female', 'F')
		)
    gander = models.CharField(max_length=6, choices=GANDER_CHOISE)
    skype = models.CharField(max_length=30)
    code_clienta = models.ForeignKey(Customer)
    stavka = models.FloatField(default=7)

    def code(self):
        return self.code_clienta

    def __unicode__(self):
        return self.user.username


    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    full_name.short_description = 'ФИО'

    User.full_name = full_name



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])



class ExpectedCargo(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.FloatField()
    date_add = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    post_delivery = models.CharField(max_length=100, blank=True, null=True)
    treck = models.CharField(max_length=50)
    comment = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey(Customer, null=True, blank=True)

    def __unicode__(self):
        return self.name
