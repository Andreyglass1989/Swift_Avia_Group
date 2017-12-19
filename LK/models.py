# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    category_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    firstname_translit = models.CharField(max_length=32)
    lastname_translit = models.CharField(max_length=32)
    company = models.CharField(max_length=40)
    region = models.CharField(max_length=128)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    dom = models.CharField(max_length=10)
    kv = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    custom_field = models.TextField()
    use = models.IntegerField()
    sandbox = models.IntegerField(blank=True, null=True)
    date_fix = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'address'

    def __str__(self):
        return self.lastname

class Address166149(models.Model):
    address_id = models.AutoField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    parcel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'address_166_149'


class AddressCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'address_category'

    def __str__(self):
        return self.name


class AddressTemp(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    category_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    firstname_translit = models.CharField(max_length=32)
    lastname_translit = models.CharField(max_length=32)
    company = models.CharField(max_length=40)
    region = models.CharField(max_length=128)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    dom = models.CharField(max_length=10)
    kv = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    custom_field = models.TextField()
    use = models.IntegerField()
    sandbox = models.IntegerField(blank=True, null=True)
    date_fix = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'address_temp'


class Affiliate(models.Model):
    affiliate_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    company = models.CharField(max_length=40)
    website = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    code = models.CharField(max_length=64)
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    tax = models.CharField(max_length=64)
    payment = models.CharField(max_length=6)
    cheque = models.CharField(max_length=100)
    paypal = models.CharField(max_length=64)
    bank_name = models.CharField(max_length=64)
    bank_branch_number = models.CharField(max_length=64)
    bank_swift_code = models.CharField(max_length=64)
    bank_account_name = models.CharField(max_length=64)
    bank_account_number = models.CharField(max_length=64)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate'


class AffiliateActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_activity'


class AffiliateLogin(models.Model):
    affiliate_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_login'


class AffiliateTransaction(models.Model):
    affiliate_transaction_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_transaction'


class Air(models.Model):
    air_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField()
    air_status_id = models.IntegerField()
    sklad_id = models.IntegerField()
    date_departure = models.DateField()
    date_arrival = models.DateField()
    date_doc = models.DateTimeField()
    date_gruz = models.DateField()
    sandbox = models.IntegerField(blank=True, null=True)
    xtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'air'

    def __str__(self):
        return self.name

class AirHistory(models.Model):
    air_history_id = models.AutoField(primary_key=True)
    air_id = models.IntegerField()
    user_id = models.IntegerField()
    air_status_id = models.IntegerField()
    date_added = models.DateTimeField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'air_history'


class AirParcel(models.Model):
    air_parcel_id = models.AutoField(primary_key=True)
    air_id = models.IntegerField()
    parcel_id = models.IntegerField()
    address_id = models.IntegerField(blank=True, null=True)
    customer_recipient = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'air_parcel'


class Api(models.Model):
    api_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    password = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api'


class Attribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attribute'


class AttributeDescription(models.Model):
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'attribute_description'
        unique_together = (('attribute_id', 'language_id'),)


class AttributeGroup(models.Model):
    attribute_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attribute_group'


class AttributeGroupDescription(models.Model):
    attribute_group_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'attribute_group_description'
        unique_together = (('attribute_group_id', 'language_id'),)


class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banner'


class BannerImage(models.Model):
    banner_image_id = models.AutoField(primary_key=True)
    banner_id = models.IntegerField()
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banner_image'


class BannerImageDescription(models.Model):
    banner_image_id = models.IntegerField()
    language_id = models.IntegerField()
    banner_id = models.IntegerField()
    title = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'banner_image_description'
        unique_together = (('banner_image_id', 'language_id'),)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'


class CategoryDescription(models.Model):
    category_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category_description'
        unique_together = (('category_id', 'language_id'),)


class CategoryFilter(models.Model):
    category_id = models.IntegerField()
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_filter'
        unique_together = (('category_id', 'filter_id'),)


class CategoryGroup(models.Model):
    category_group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    alarm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_group'

    def __unicode__(self):
        return self.name

class CategoryPath(models.Model):
    category_id = models.IntegerField()
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_path'
        unique_together = (('category_id', 'path_id'),)


class CategoryToLayout(models.Model):
    category_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_to_layout'
        unique_together = (('category_id', 'store_id'),)


class CategoryToStore(models.Model):
    category_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_to_store'
        unique_together = (('category_id', 'store_id'),)


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    iso_code_2 = models.CharField(max_length=2)
    iso_code_3 = models.CharField(max_length=3)
    address_format = models.TextField()
    postcode_required = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'country'

    def __unicode__(self):
        return self.name


class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=10)
    type = models.CharField(max_length=1)
    discount = models.DecimalField(max_digits=15, decimal_places=4)
    logged = models.IntegerField()
    shipping = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()
    uses_total = models.IntegerField()
    uses_customer = models.CharField(max_length=11)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupon'


class CouponCategory(models.Model):
    coupon_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon_category'
        unique_together = (('coupon_id', 'category_id'),)


class CouponHistory(models.Model):
    coupon_history_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupon_history'


class CouponProduct(models.Model):
    coupon_product_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon_product'


class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    symbol_left = models.CharField(max_length=12)
    symbol_right = models.CharField(max_length=12)
    decimal_place = models.CharField(max_length=1)
    value = models.FloatField()
    status = models.IntegerField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'currency'

    def __str__(self):
        return self.code


class CustomField(models.Model):
    custom_field_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    value = models.TextField()
    location = models.CharField(max_length=7)
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_field'


class CustomFieldCustomerGroup(models.Model):
    custom_field_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_field_customer_group'
        unique_together = (('custom_field_id', 'customer_group_id'),)


class CustomFieldDescription(models.Model):
    custom_field_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'custom_field_description'
        unique_together = (('custom_field_id', 'language_id'),)


class CustomFieldValue(models.Model):
    custom_field_value_id = models.AutoField(primary_key=True)
    custom_field_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_field_value'


class CustomFieldValueDescription(models.Model):
    custom_field_value_id = models.IntegerField()
    language_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'custom_field_value_description'
        unique_together = (('custom_field_value_id', 'language_id'),)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_number = models.CharField(max_length=20)
    customer_group_id = models.IntegerField()
    store_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    cart = models.TextField(blank=True, null=True)
    wishlist = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField()
    address_id = models.IntegerField()
    custom_field = models.TextField()
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    safe = models.IntegerField()
    token = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    external_id = models.CharField(max_length=32)
    partner_id = models.IntegerField()
    comment_customer = models.TextField()
    sandbox = models.IntegerField()
    color = models.TextField()
    typ = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.external_id

    def full_name(self):
        return self.firstname+' '+self.lastname

class CustomerActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_activity'


class CustomerBanIp(models.Model):
    customer_ban_ip_id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'customer_ban_ip'


class CustomerContact(models.Model):
    customer_contact_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    contact_type_id = models.IntegerField()
    value = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'customer_contact'


class CustomerGroup(models.Model):
    customer_group_id = models.AutoField(primary_key=True)
    approval = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_group'


class CustomerGroupDescription(models.Model):
    customer_group_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'customer_group_description'
        unique_together = (('customer_group_id', 'language_id'),)


class CustomerHistory(models.Model):
    customer_history_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_history'


class CustomerIp(models.Model):
    customer_ip_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_ip'


class CustomerLogin(models.Model):
    customer_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_login'


class CustomerOnline(models.Model):
    ip = models.CharField(primary_key=True, max_length=40)
    customer_id = models.IntegerField()
    url = models.TextField()
    referer = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_online'


CITY_CHOICES = (
    ('Cherkassi', 'Cherkassi'),
    ('Chernigov', 'Chernigov'),
    ('Chernovtsu', 'Chernovtsu'),
    ('Dnepropetrovsk', 'Dnepropetrovsk'),
    ('Ivano-Frankovsk', 'Ivano-Frankovsk'),
    ('Kharkiv', 'Kharkiv'),
    ('Kherson', 'Kherson'),
    ('Khmelnitskij', 'Khmelnitskij'),
    ('Kiev', 'Kiev'),
    ('Kirovograd', 'Kirovograd'),
    ('Lviv', 'Lviv'),
    ('Lutsk', 'Lutsk'),
    ('Nikolaev', 'Nikolaev'),
    ('Odessa', 'Odessa'),
    ('Rovno', 'Rovno'),
    ('Sumu', 'Sumu'),
    ('Ternopol', 'Ternopol'),
    ('Uzhgorod', 'Uzhgorod'),
    ('Vinnitsa', 'Vinnitsa'),
    ("Zaporozh'e", "Zaporozh'e"),
    ("Zhitomir", "Zhitomir"),
)
kirill = RegexValidator(r'^[a-zA-Z]+$')
cifra = RegexValidator(r'^[0-9]+$')
class CustomerRecipients(models.Model):
    cr_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, null=True, blank=True)  #_id
    country = models.ForeignKey(Country, default=220, null=True, blank=True) #_id
    name = models.CharField(max_length=255, validators=[kirill], error_messages = {'invalid': ("Только символы латинского алфавита (a–z, A-Z).")})
    lastname = models.CharField(max_length=255, validators=[kirill], error_messages = {'invalid': ("Только символы латинского алфавита (a–z, A-Z).")})
    city = models.CharField(max_length=255, choices=CITY_CHOICES, default='Kiev')
    street = models.CharField(max_length=255, validators=[kirill], error_messages = {'invalid': ("Только символы латинского алфавита (a–z, A-Z).")})
    home = models.IntegerField(validators=[cifra], error_messages = {'invalid': ("Только цифры (0-9).")})
    room = models.IntegerField(blank = True, validators=[cifra], error_messages = {'invalid': ("Только цифры (0-9).")})
    phone = models.CharField(max_length=255, validators=[cifra], error_messages = {'invalid': ("Только цифры (0-9).")})
    pos_item = models.IntegerField(blank=True, null=True)
    pochtamat_id = models.IntegerField(blank=True, null=True)
    date_fix = models.DateTimeField(auto_now=True)
    #disabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_recipients'

    def __unicode__(self):
        return self.lastname + ' ' + self.name


class CustomerReward(models.Model):
    customer_reward_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_reward'


class CustomerTransaction(models.Model):
    customer_transaction_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_transaction'


class Download(models.Model):
    download_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=128)
    mask = models.CharField(max_length=128)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'download'


class DownloadDescription(models.Model):
    download_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'download_description'
        unique_together = (('download_id', 'language_id'),)


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    trigger = models.TextField()
    action = models.TextField()

    class Meta:
        managed = False
        db_table = 'event'


class Extension(models.Model):
    extension_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'extension'


class ExternalId(models.Model):
    autoinc_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'external_id'


class Filter(models.Model):
    filter_id = models.AutoField(primary_key=True)
    filter_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filter'


class FilterDescription(models.Model):
    filter_id = models.IntegerField()
    language_id = models.IntegerField()
    filter_group_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'filter_description'
        unique_together = (('filter_id', 'language_id'),)


class FilterGroup(models.Model):
    filter_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filter_group'


class FilterGroupDescription(models.Model):
    filter_group_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'filter_group_description'
        unique_together = (('filter_group_id', 'language_id'),)


class GeoZone(models.Model):
    geo_zone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_modified = models.DateTimeField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'geo_zone'


class Information(models.Model):
    information_id = models.AutoField(primary_key=True)
    bottom = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'information'


class InformationCategory(models.Model):
    information_category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'information_category'


class InformationCategoryDescription(models.Model):
    information_category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'information_category_description'


class InformationCategoryToLayout(models.Model):
    information_category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'information_category_to_layout'


class InformationCategoryToStore(models.Model):
    information_category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'information_category_to_store'


class InformationDescription(models.Model):
    information_id = models.IntegerField()
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'information_description'
        unique_together = (('information_id', 'language_id'),)


class InformationToCategory(models.Model):
    information_category_id = models.IntegerField()
    information_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'information_to_category'


class InformationToLayout(models.Model):
    information_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'information_to_layout'
        unique_together = (('information_id', 'store_id'),)


class InformationToStore(models.Model):
    information_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'information_to_store'
        unique_together = (('information_id', 'store_id'),)


class ItemClass(models.Model):
    item_class_id = models.AutoField(primary_key=True)
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_class'


class ItemClassDescription(models.Model):
    item_class_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'item_class_description'
        unique_together = (('item_class_id', 'language_id'),)


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=5)
    locale = models.CharField(max_length=255)
    image = models.CharField(max_length=64)
    directory = models.CharField(max_length=32)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'language'


class Layout(models.Model):
    layout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'layout'


class LayoutModule(models.Model):
    layout_module_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    code = models.CharField(max_length=64)
    position = models.CharField(max_length=14)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'layout_module'


class LayoutRoute(models.Model):
    layout_route_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    store_id = models.IntegerField()
    route = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'layout_route'


class LengthClass(models.Model):
    length_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'length_class'


class LengthClassDescription(models.Model):
    length_class_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'length_class_description'
        unique_together = (('length_class_id', 'language_id'),)


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address = models.TextField()
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    geocode = models.CharField(max_length=32)
    image = models.CharField(max_length=255, blank=True, null=True)
    open = models.TextField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'location'


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    pack_number = models.CharField(max_length=20)
    parcel_number = models.CharField(max_length=20)
    air_name = models.CharField(max_length=20)
    user_id = models.IntegerField()
    status_id = models.IntegerField()
    item_id = models.IntegerField()
    type_id = models.CharField(max_length=20)
    action = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'log'


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manufacturer'


class ManufacturerToStore(models.Model):
    manufacturer_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manufacturer_to_store'
        unique_together = (('manufacturer_id', 'store_id'),)


class Marketing(models.Model):
    marketing_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    code = models.CharField(max_length=64)
    clicks = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marketing'


class Modification(models.Model):
    modification_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    version = models.CharField(max_length=32)
    link = models.CharField(max_length=255)
    xml = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modification'


class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32)
    setting = models.TextField()

    class Meta:
        managed = False
        db_table = 'module'


class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'option'


class OptionDescription(models.Model):
    option_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'option_description'
        unique_together = (('option_id', 'language_id'),)


class OptionValue(models.Model):
    option_value_id = models.AutoField(primary_key=True)
    option_id = models.IntegerField()
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'option_value'


class OptionValueDescription(models.Model):
    option_value_id = models.IntegerField()
    language_id = models.IntegerField()
    option_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'option_value_description'
        unique_together = (('option_value_id', 'language_id'),)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField()
    invoice_prefix = models.CharField(max_length=26)
    store_id = models.IntegerField()
    store_name = models.CharField(max_length=64)
    store_url = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    custom_field = models.TextField()
    payment_firstname = models.CharField(max_length=32)
    payment_lastname = models.CharField(max_length=32)
    payment_company = models.CharField(max_length=40)
    payment_address_1 = models.CharField(max_length=128)
    payment_address_2 = models.CharField(max_length=128)
    payment_city = models.CharField(max_length=128)
    payment_postcode = models.CharField(max_length=10)
    payment_country = models.CharField(max_length=128)
    payment_country_id = models.IntegerField()
    payment_zone = models.CharField(max_length=128)
    payment_zone_id = models.IntegerField()
    payment_address_format = models.TextField()
    payment_custom_field = models.TextField()
    payment_method = models.CharField(max_length=128)
    payment_code = models.CharField(max_length=128)
    shipping_firstname = models.CharField(max_length=32)
    shipping_lastname = models.CharField(max_length=32)
    shipping_company = models.CharField(max_length=40)
    shipping_address_1 = models.CharField(max_length=128)
    shipping_address_2 = models.CharField(max_length=128)
    shipping_city = models.CharField(max_length=128)
    shipping_postcode = models.CharField(max_length=10)
    shipping_country = models.CharField(max_length=128)
    shipping_country_id = models.IntegerField()
    shipping_zone = models.CharField(max_length=128)
    shipping_zone_id = models.IntegerField()
    shipping_address_format = models.TextField()
    shipping_custom_field = models.TextField()
    shipping_method = models.CharField(max_length=128)
    shipping_code = models.CharField(max_length=128)
    comment = models.TextField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    order_status_id = models.IntegerField()
    affiliate_id = models.IntegerField()
    commission = models.DecimalField(max_digits=15, decimal_places=4)
    marketing_id = models.IntegerField()
    tracking = models.CharField(max_length=64)
    language_id = models.IntegerField()
    currency_id = models.IntegerField()
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=15, decimal_places=8)
    ip = models.CharField(max_length=40)
    forwarded_ip = models.CharField(max_length=40)
    user_agent = models.CharField(max_length=255)
    accept_language = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order'


class OrderCustomField(models.Model):
    order_custom_field_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    custom_field_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)
    location = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'order_custom_field'


class OrderFraud(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    country_match = models.CharField(max_length=3)
    country_code = models.CharField(max_length=2)
    high_risk_country = models.CharField(max_length=3)
    distance = models.IntegerField()
    ip_region = models.CharField(max_length=255)
    ip_city = models.CharField(max_length=255)
    ip_latitude = models.DecimalField(max_digits=10, decimal_places=6)
    ip_longitude = models.DecimalField(max_digits=10, decimal_places=6)
    ip_isp = models.CharField(max_length=255)
    ip_org = models.CharField(max_length=255)
    ip_asnum = models.IntegerField()
    ip_user_type = models.CharField(max_length=255)
    ip_country_confidence = models.CharField(max_length=3)
    ip_region_confidence = models.CharField(max_length=3)
    ip_city_confidence = models.CharField(max_length=3)
    ip_postal_confidence = models.CharField(max_length=3)
    ip_postal_code = models.CharField(max_length=10)
    ip_accuracy_radius = models.IntegerField()
    ip_net_speed_cell = models.CharField(max_length=255)
    ip_metro_code = models.IntegerField()
    ip_area_code = models.IntegerField()
    ip_time_zone = models.CharField(max_length=255)
    ip_region_name = models.CharField(max_length=255)
    ip_domain = models.CharField(max_length=255)
    ip_country_name = models.CharField(max_length=255)
    ip_continent_code = models.CharField(max_length=2)
    ip_corporate_proxy = models.CharField(max_length=3)
    anonymous_proxy = models.CharField(max_length=3)
    proxy_score = models.IntegerField()
    is_trans_proxy = models.CharField(max_length=3)
    free_mail = models.CharField(max_length=3)
    carder_email = models.CharField(max_length=3)
    high_risk_username = models.CharField(max_length=3)
    high_risk_password = models.CharField(max_length=3)
    bin_match = models.CharField(max_length=10)
    bin_country = models.CharField(max_length=2)
    bin_name_match = models.CharField(max_length=3)
    bin_name = models.CharField(max_length=255)
    bin_phone_match = models.CharField(max_length=3)
    bin_phone = models.CharField(max_length=32)
    customer_phone_in_billing_location = models.CharField(max_length=8)
    ship_forward = models.CharField(max_length=3)
    city_postal_match = models.CharField(max_length=3)
    ship_city_postal_match = models.CharField(max_length=3)
    score = models.DecimalField(max_digits=10, decimal_places=5)
    explanation = models.TextField()
    risk_score = models.DecimalField(max_digits=10, decimal_places=5)
    queries_remaining = models.IntegerField()
    maxmind_id = models.CharField(max_length=8)
    error = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_fraud'


class OrderHistory(models.Model):
    order_history_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_history'


class OrderOption(models.Model):
    order_option_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_product_id = models.IntegerField()
    product_option_id = models.IntegerField()
    product_option_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'order_option'


class OrderProduct(models.Model):
    order_product_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    tax = models.DecimalField(max_digits=15, decimal_places=4)
    reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_product'


class OrderRecurring(models.Model):
    order_recurring_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    recurring_id = models.IntegerField()
    recurring_name = models.CharField(max_length=255)
    recurring_description = models.CharField(max_length=255)
    recurring_frequency = models.CharField(max_length=25)
    recurring_cycle = models.SmallIntegerField()
    recurring_duration = models.SmallIntegerField()
    recurring_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial = models.IntegerField()
    trial_frequency = models.CharField(max_length=25)
    trial_cycle = models.SmallIntegerField()
    trial_duration = models.SmallIntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_recurring'


class OrderRecurringTransaction(models.Model):
    order_recurring_transaction_id = models.AutoField(primary_key=True)
    order_recurring_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_recurring_transaction'


class OrderStatus(models.Model):
    order_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'order_status'
        unique_together = (('order_status_id', 'language_id'),)


class OrderTotal(models.Model):
    order_total_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_total'


class OrderVoucher(models.Model):
    order_voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    voucher_id = models.IntegerField()
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'order_voucher'

class PackStatus(models.Model):
    pack_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    sms_text = models.CharField(max_length=160)
    customer_notify = models.IntegerField()
    next_status_text = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pack_status'
        unique_together = (('pack_status_id', 'language_id'),)

    def __unicode__(self):
        return self.name



class Sklad(models.Model):
    sklad_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sklad'

    def __unicode__(self):
        return self.name


class Pack(models.Model):
    pack_id = models.AutoField(primary_key=True)
    pack_number = models.IntegerField(default=191100000)   #
    external_id = models.CharField(max_length=16)   #++++++++++++++++++++
    date_added = models.DateTimeField(auto_now_add=True)#++++++++++++++++
    customer = models.ForeignKey(Customer)          #++++++++++++++++++++_id
    sklad = models.ForeignKey(Sklad)             #++++++++++++++++++++ id
    pack_status = models.ForeignKey(PackStatus)     #++++++++++++++++++++_id
    total = models.FloatField(blank=True, null=True)                     #++++++++++++++++++++
    volume = models.FloatField(blank=True, null=True)           #++++++++++++++++++++
    weight = models.FloatField(blank=False, null=False)                    #++++++++++++++++++++
    point = models.IntegerField(blank=False, null=False)                   #++++++++++++++++++++
    language = models.ForeignKey(Language, default=2)#+++++++++++++++++++  id
    currency = models.ForeignKey(Currency)          #++++++++++++++++++++ id
    currency_code = models.CharField(max_length=3, default='USD')#+++++++
    currency_value = models.FloatField(default=1, blank=True, null=True)   #++++++++++++++++++++
    comment = models.TextField(blank=True, null=True)                    #++++++++++++++++++++
    category_group = models.ForeignKey(CategoryGroup, default=3)#+++++++++++++++++
    sandbox = models.IntegerField(default=0, blank=True, null=True)         #+++++++++++++++++++
    def_field = models.IntegerField(db_column='def', default=0, blank=True, null=True)  # Field renamed because it was a Python reserved word.                          #+++++++++++++++++++
    packlist = models.IntegerField(default=0, blank=True, null=True)        #+++++++++++++++++++
    ttn = models.CharField(max_length=20, blank=False, null=False) #+++++++++++++++++++
   # document_file = models.FileField(null=True, blank=True)


    class Meta:
        managed = False
        db_table = 'pack'
        ordering = ["-date_added"]

    def __str__(self):
        return self.pack_number

class PackHistory(models.Model):
    pack_history_id = models.AutoField(primary_key=True)
    pack_id = models.IntegerField()
    pack_status_id = models.IntegerField()
    use = models.IntegerField()
    notify = models.IntegerField()
    date_added = models.DateTimeField()
    comment = models.TextField()
    user_id = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'pack_history'


class PackProduct(models.Model):
    pack_product_id = models.AutoField(primary_key=True)
    pack = models.ForeignKey(Pack)                       #_id
    name = models.CharField(verbose_name='*Наименование товара',max_length=255)
    price = models.FloatField(verbose_name='*Цена/ед.')
    quantity = models.IntegerField(verbose_name='*Кол-во')
    item_class_id = models.IntegerField(default=0, null=True, blank=True)
    weight = models.FloatField(verbose_name='*Вес', null=True, blank=True)
    weight_netto = models.FloatField(default=0, null=True, blank=True)
    volume = models.FloatField(default=0, null=True, blank=True)
    point = models.IntegerField(verbose_name='*Мест', null=True, blank=True)
    url = models.CharField(verbose_name='Ссылка', max_length=255, null=True, blank=True)
    packed_quantity = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'pack_product'

    def __str__(self):
        return self.name.encode('utf8')


class PackProductChild(models.Model):
    pack_product_child_id = models.AutoField(primary_key=True)
    pack_id = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    item_class_id = models.IntegerField()
    weight = models.FloatField()
    weight_netto = models.FloatField()
    volume = models.FloatField()
    point = models.IntegerField()
    url = models.CharField(max_length=255)
    packed_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pack_product_child'


#----------------PackStatus----------


class PacklistProduct(models.Model):
    pack_product_id = models.AutoField(primary_key=True)
    pack_id = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    weight = models.FloatField()
    weight_netto = models.FloatField()
    volume = models.FloatField()
    point = models.IntegerField()
    url = models.CharField(max_length=255)
    packed_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'packlist_product'


class Parcel(models.Model):
    parcel_id = models.AutoField(primary_key=True)
    parcel_number = models.CharField(max_length=20)
    parcel_status = models.ForeignKey(PackStatus)
    sklad_id = models.IntegerField()
    date_added = models.DateTimeField()
    weight = models.FloatField()
    weight_b = models.FloatField()
    point = models.IntegerField()
    total = models.FloatField()
    comment = models.TextField()
    external_id = models.IntegerField()
    sandbox = models.IntegerField(blank=True, null=True)
    volume = models.FloatField()
    width = models.DecimalField(max_digits=15, decimal_places=2)
    height = models.DecimalField(max_digits=15, decimal_places=2)
    length = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'parcel'


class ParcelHistory(models.Model):
    parcel_history_id = models.AutoField(primary_key=True)
    parcel_id = models.IntegerField()
    parcel_status_id = models.IntegerField()
    use = models.IntegerField()
    notify = models.IntegerField()
    date_added = models.DateTimeField()
    comment = models.TextField()
    user_id = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'parcel_history'


class ParcelPackProduct(models.Model):
    parcel_pack_product_id = models.AutoField(primary_key=True)
    parcel_id = models.IntegerField()
    pack_product_id = models.IntegerField()
    pack_id = models.IntegerField()
    quantity = models.IntegerField()
    weight = models.FloatField()
    point = models.IntegerField()
    loss = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parcel_pack_product'


class ParcelStatus(models.Model):
    parcel_status_id = models.AutoField(primary_key=True)
    pack_status_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'parcel_status'
        unique_together = (('parcel_status_id', 'language_id'),)


class ParcelUa(models.Model):
    parcel_ua_id = models.AutoField(primary_key=True)
    air_id = models.IntegerField(unique=True)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'parcel_ua'


class ParcelUaData(models.Model):
    parcel_ua_id = models.IntegerField()
    plomba_id = models.IntegerField()
    width = models.DecimalField(max_digits=4, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.DecimalField(max_digits=4, decimal_places=2)
    volume = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'parcel_ua_data'
        unique_together = (('parcel_ua_id', 'plomba_id'),)


class Partner(models.Model):
    partner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    api_key = models.CharField(max_length=64)
    status = models.IntegerField()
    prefix = models.CharField(max_length=10)
    prefix_kleint = models.CharField(max_length=2)
    sms_name = models.CharField(max_length=11)
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'partner'


class PartnerInc0(models.Model):
    autoinc_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'partner_inc_0'


class PartnerInc0Sandbox(models.Model):
    autoinc_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'partner_inc_0_sandbox'


class PartnerInc1Sandbox(models.Model):
    autoinc_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'partner_inc_1_sandbox'


class PartnerInc2Sandbox(models.Model):
    autoinc_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'partner_inc_2_sandbox'


class PartnerInc3Sandbox(models.Model):
    autoinc_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'partner_inc_3_sandbox'


class PdTheme(models.Model):
    key = models.CharField(unique=True, max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'pd_theme'


class PlombaDimension(models.Model):
    plomba_id = models.IntegerField(primary_key=True)
    plomba_width = models.DecimalField(max_digits=4, decimal_places=2)
    plomba_height = models.DecimalField(max_digits=4, decimal_places=2)
    plomba_length = models.DecimalField(max_digits=4, decimal_places=2)
    plomba_weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'plomba_dimension'




class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=64)
    sku = models.CharField(max_length=64)
    upc = models.CharField(max_length=12)
    ean = models.CharField(max_length=14)
    jan = models.CharField(max_length=13)
    isbn = models.CharField(max_length=17)
    mpn = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    quantity = models.IntegerField()
    stock_status_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.IntegerField()
    shipping = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    points = models.IntegerField()
    tax_class_id = models.IntegerField()
    date_available = models.DateField()
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_class_id = models.IntegerField()
    length = models.DecimalField(max_digits=15, decimal_places=8)
    width = models.DecimalField(max_digits=15, decimal_places=8)
    height = models.DecimalField(max_digits=15, decimal_places=8)
    length_class_id = models.IntegerField()
    subtract = models.IntegerField()
    minimum = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    viewed = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product'


class ProductAttribute(models.Model):
    product_id = models.IntegerField()
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'product_attribute'
        unique_together = (('product_id', 'attribute_id', 'language_id'),)


class ProductDescription(models.Model):
    product_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_description'
        unique_together = (('product_id', 'language_id'),)


class ProductDiscount(models.Model):
    product_discount_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    quantity = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'product_discount'


class ProductFilter(models.Model):
    product_id = models.IntegerField()
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_filter'
        unique_together = (('product_id', 'filter_id'),)


class ProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_image'


class ProductOption(models.Model):
    product_option_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    value = models.TextField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_option'


class ProductOptionValue(models.Model):
    product_option_value_id = models.AutoField(primary_key=True)
    product_option_id = models.IntegerField()
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value_id = models.IntegerField()
    quantity = models.IntegerField()
    subtract = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    price_prefix = models.CharField(max_length=1)
    points = models.IntegerField()
    points_prefix = models.CharField(max_length=1)
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_prefix = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'product_option_value'


class ProductRecurring(models.Model):
    product_id = models.IntegerField()
    recurring_id = models.IntegerField()
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_recurring'
        unique_together = (('product_id', 'recurring_id', 'customer_group_id'),)


class ProductRelated(models.Model):
    product_id = models.IntegerField()
    related_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_related'
        unique_together = (('product_id', 'related_id'),)


class ProductReward(models.Model):
    product_reward_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_reward'


class ProductSpecial(models.Model):
    product_special_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'product_special'


class ProductToCategory(models.Model):
    product_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_to_category'
        unique_together = (('product_id', 'category_id'),)


class ProductToDownload(models.Model):
    product_id = models.IntegerField()
    download_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_to_download'
        unique_together = (('product_id', 'download_id'),)


class ProductToLayout(models.Model):
    product_id = models.IntegerField()
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_to_layout'
        unique_together = (('product_id', 'store_id'),)


class ProductToStore(models.Model):
    product_id = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_to_store'
        unique_together = (('product_id', 'store_id'),)


class Recurring(models.Model):
    recurring_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    frequency = models.CharField(max_length=10)
    duration = models.IntegerField()
    cycle = models.IntegerField()
    trial_status = models.IntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial_frequency = models.CharField(max_length=10)
    trial_duration = models.IntegerField()
    trial_cycle = models.IntegerField()
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recurring'


class RecurringDescription(models.Model):
    recurring_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'recurring_description'
        unique_together = (('recurring_id', 'language_id'),)


class Return(models.Model):
    return_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    product = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    opened = models.IntegerField()
    return_reason_id = models.IntegerField()
    return_action_id = models.IntegerField()
    return_status_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_ordered = models.DateField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'return'


class ReturnAction(models.Model):
    return_action_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'return_action'
        unique_together = (('return_action_id', 'language_id'),)


class ReturnHistory(models.Model):
    return_history_id = models.AutoField(primary_key=True)
    return_id = models.IntegerField()
    return_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'return_history'


class ReturnReason(models.Model):
    return_reason_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'return_reason'
        unique_together = (('return_reason_id', 'language_id'),)


class ReturnStatus(models.Model):
    return_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'return_status'
        unique_together = (('return_status_id', 'language_id'),)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    author = models.CharField(max_length=64)
    text = models.TextField()
    rating = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'review'


class Setting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    code = models.CharField(max_length=32)
    key = models.CharField(max_length=64)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'setting'


class SimpleCustomData(models.Model):
    object_type = models.IntegerField()
    object_id = models.IntegerField()
    customer_id = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'simple_custom_data'
        unique_together = (('object_type', 'object_id', 'customer_id'),)




class Sms(models.Model):
    sms_id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField()
    date_send = models.DateTimeField()
    destination = models.CharField(max_length=64)
    message = models.CharField(max_length=160)
    sender = models.CharField(max_length=11)
    params = models.TextField()
    status = models.IntegerField()
    result = models.TextField()
    date_locked = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sms'


class StockStatus(models.Model):
    stock_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'stock_status'
        unique_together = (('stock_status_id', 'language_id'),)


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    ssl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'store'


class TaxClass(models.Model):
    tax_class_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tax_class'


class TaxRate(models.Model):
    tax_rate_id = models.AutoField(primary_key=True)
    geo_zone_id = models.IntegerField()
    name = models.CharField(max_length=32)
    rate = models.DecimalField(max_digits=15, decimal_places=4)
    type = models.CharField(max_length=1)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tax_rate'


class TaxRateToCustomerGroup(models.Model):
    tax_rate_id = models.IntegerField()
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tax_rate_to_customer_group'
        unique_together = (('tax_rate_id', 'customer_group_id'),)


class TaxRule(models.Model):
    tax_rule_id = models.AutoField(primary_key=True)
    tax_class_id = models.IntegerField()
    tax_rate_id = models.IntegerField()
    based = models.CharField(max_length=10)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tax_rule'


class Upload(models.Model):
    upload_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'upload'


class UrlAlias(models.Model):
    url_alias_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'url_alias'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_group_id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    image = models.CharField(max_length=255)
    code = models.CharField(max_length=40)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    date_added = models.DateTimeField()
    sandbox = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.username


class UserAccess(models.Model):
    user_id = models.IntegerField()
    group = models.CharField(max_length=32)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_access'
        unique_together = (('user_id', 'group'),)


class UserGroup(models.Model):
    user_group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    permission = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_group'


class UserGroupAccess(models.Model):
    route = models.CharField(max_length=64)
    user_group_id = models.IntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_group_access'


class Voucher(models.Model):
    voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'voucher'


class VoucherHistory(models.Model):
    voucher_history_id = models.AutoField(primary_key=True)
    voucher_id = models.IntegerField()
    order_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'voucher_history'


class VoucherTheme(models.Model):
    voucher_theme_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'voucher_theme'


class VoucherThemeDescription(models.Model):
    voucher_theme_id = models.IntegerField()
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'voucher_theme_description'
        unique_together = (('voucher_theme_id', 'language_id'),)


class WeightClass(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'weight_class'


class WeightClassDescription(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'weight_class_description'
        unique_together = (('weight_class_id', 'language_id'),)


class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zone'

    def __unicode__(self):
        return self.name


class ZoneToGeoZone(models.Model):
    zone_to_geo_zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    geo_zone_id = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zone_to_geo_zone'

