# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from LK.models import Customer, Pack, Air, PlombaDimension, PackProduct
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

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
    # class Meta():
    #     db_table= 'File' #u'Отзывы клиентов'

    name = models.CharField(max_length = 50)     
    document = models.FileField(null=True, blank=True)
    packid = models.ForeignKey(Pack)
    image = models.ImageField( upload_to='static/images/', null=True, blank=True )

    def __int__(self):
        return self.name

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True



class CalculatorGroup(models.Model):
    # class Meta():
    #     db_table = 'CalculatorGroup'

    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __unicode__(self):
        return self.name

class LossInAir(models.Model):

    air             = models.ForeignKey(Air)
    plomba_number   = models.ForeignKey(PlombaDimension)
    customer        = models.ForeignKey(Customer)
    weight_loss     = models.FloatField(null=True, blank=True)
    name_tovar      = models.ForeignKey(PackProduct)
    quantity        = models.IntegerField(null=True, blank=True)
    price_our       = models.FloatField(null=True, blank=True)
    price_client    = models.FloatField(null=True, blank=True)
    comment         = models.CharField(max_length=150)
    date_shortages  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_tovar.encode('utf8')


class CustomerNovaPoshta(models.Model):

    customer        = models.ForeignKey(Customer)
    city            = models.CharField(max_length=50)
    address_client  = models.CharField(max_length=200)
    name            = models.CharField(max_length=200)
    phone           = models.CharField(max_length=13, validators=[MinLengthValidator(10)])
    comment         = models.CharField(max_length=150, null=True, blank=True)

    def __unicode__(self):
        return self.name

        

class PackCustomer(models.Model):

    customer        = models.ForeignKey(Customer)
    name            = models.CharField(max_length=150, null=True, blank=True)
    description     = models.CharField(max_length=200, null=True, blank=True)
    model_number    = models.CharField(max_length=200, null=True, blank=True)
    url1            = models.CharField(max_length=250, null=True, blank=True)
    url2            = models.CharField(max_length=250, null=True, blank=True)
    word_search     = models.CharField(max_length=150, null=True, blank=True)
    date_added      = models.DateTimeField(auto_now=True)
    sender          = models.CharField(max_length=250, null=True, blank=True)
    company_transporter  = models.CharField(max_length=250, null=True, blank=True)
    recipient_our   = models.CharField(max_length=250, null=True, blank=True)
    phone_recip     = models.CharField(max_length=250, null=True, blank=True)
    #comment         = models.CharField(max_length=150, null=True, blank=True)

    def __unicode__(self):
        return self.name




class Blog(models.Model):
    title = models.CharField(max_length=200)
    date_add = models.DateField(auto_now=True)
    image = models.ImageField( upload_to='static/images/blog/', null=True, blank=True )
    text = models.TextField()


    def __unicode__(self):
        return self.title

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Изображение'
    image_img.allow_tags = True







class Buyout(models.Model):
    url      = models.CharField(max_length=255)
    name     = models.CharField(max_length=100)
    quantity = models.IntegerField(blank=True, null=True)
    price    = models.FloatField(blank=True, null=True)
    size     = models.CharField(max_length=50, blank=True, null=True)
    color    = models.CharField(max_length=100, blank=True, null=True)
    comment  = models.CharField(max_length=255, blank=True, null=True)
    image    = models.ImageField(upload_to='static/images/Buyout', null=True, blank=True)
    customer = models.ForeignKey(Customer)
    # treck_num= models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now=True)
    # date_add_parent = models.DateTimeField(auto_now_add=True)
    STATUS_BUYOUT_CHOISE =(
    ('Создан', 'Создан'),    
    ('Оплачен', 'Оплачен'),
    ('Выкуплено', 'Выкуплено'),
    ('Ожидаеться на складе', 'Ожидаеться на складе'),
    ('Доставлен на склад', 'Доставлен на склад'),
    ('Летит в Украину', 'Летит в Украину'),
    ('Отправлен клиенту', 'Отправлен клиенту'),
    ('Нет в наличии', 'Нет в наличии'),
    )
    status   = models.CharField(choices=STATUS_BUYOUT_CHOISE, max_length=50, default='Создан')
    sum_buyout = models.FloatField(verbose_name="сумма выкупа", blank=True, null=True, default = 0.00)
    amount_shipping = models.FloatField(verbose_name="сумма за доставку", blank=True, null=True)
    track = models.CharField(verbose_name="трек", max_length=20, blank=True, null=True)

    def __unicode__(self):
        return self.name


    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True





class ManagerCustomerProfile(models.Model):
    manager = models.ForeignKey(User, limit_choices_to={'groups__name': "Менеджеры"})
    customer = models.ForeignKey(Customer)
    # phone = models.CharField(max_length=15)
    # GANDER_CHOISE =(
    #     ('Male', 'M'),
    #     ('Female', 'F')
    #     )
    # gander = models.CharField(max_length=6, choices=GANDER_CHOISE)
    # skype = models.CharField(max_length=30)
    # code_clienta = models.ForeignKey(Customer)
    # stavka = models.FloatField(default=7)

    def code(self):
        return self.customer

    # def id_client(self):
    #     return self.customer

    def __unicode__(self):
        return self.manager.username


    # def full_name(self):
    #     return '%s %s' % (self.first_name, self.last_name)

    # full_name.short_description = 'ФИО'

    # User.full_name = full_name


class AirDataUploadFrom1C(models.Model):
    # customer = models.ForeignKey(Customer, related_name="customer")
    customer = models.CharField(max_length=50)
    packing_1C = models.CharField(max_length=30)
    manager = models.CharField(max_length=50)
    weight = models.FloatField(blank=False, null=False)
    volume = models.FloatField(blank=True, null=True, default=0)
    cost = models.FloatField(blank=True, null=True)
    transaction_amount = models.FloatField(blank=True, null=True)
    insurance = models.FloatField(blank=True, null=True)
    china_expenses = models.FloatField(blank=True, null=True)
    packing_amount = models.FloatField(blank=True, null=True)
    additional_expense = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    one_percent_for_UAH = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)
    air = models.CharField(max_length=20, blank=True, null=True)
    comment = models.CharField(max_length=50, blank=True, null=True)
    difference = models.CharField(max_length=30, blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    # air2 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.packing_1C