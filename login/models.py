# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from LK.models import Customer, Pack
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


class Reviews(models.Model):
    class Meta():
        db_table= 'Reviews' #u'Отзывы клиентов'


    text_reviews = models.TextField(u'Добавить отзыв', max_length=250)
    reviews_client = models.ForeignKey(Customer)#verbose_name=u'Клиент'
    date_add = models.DateField(auto_now=True)
    recomend = models.BooleanField(u'Рекомендую', default=True)

    def __unicode__(self):
        return self.text_reviews


class File_document(models.Model):
    class Meta():
        db_table= 'File' #u'Отзывы клиентов'

    document = models.FileField(null=True, blank=True)
    packid = models.ForeignKey(Pack)



class CalculatorGroup(models.Model):
    # class Meta():
    #     db_table = 'CalculatorGroup'

    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __unicode__(self):
        return self.name