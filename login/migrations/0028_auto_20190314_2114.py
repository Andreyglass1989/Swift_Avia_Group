# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-03-14 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0027_auto_20190228_0938'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='AirDataUploadFrom1C',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('customer', models.CharField(max_length=50)),
        #         ('packing_1C', models.CharField(max_length=30)),
        #         ('manager', models.CharField(max_length=50)),
        #         ('weight', models.FloatField()),
        #         ('volume', models.FloatField(blank=True, default=0, null=True)),
        #         ('cost', models.FloatField(blank=True, null=True)),
        #         ('transaction_amount', models.FloatField(blank=True, null=True)),
        #         ('insurance', models.FloatField(blank=True, null=True)),
        #         ('china_expenses', models.FloatField(blank=True, null=True)),
        #         ('packing_amount', models.FloatField(blank=True, null=True)),
        #         ('additional_expense', models.FloatField(blank=True, null=True)),
        #         ('subtotal', models.FloatField(blank=True, null=True)),
        #         ('one_percent_for_UAH', models.FloatField(blank=True, null=True)),
        #         ('total', models.FloatField(blank=True, null=True)),
        #         ('date_added', models.DateTimeField(auto_now=True)),
        #         ('air', models.IntegerField()),
        #     ],
        # ),
        # migrations.AlterField(
        #     model_name='buyout',
        #     name='amount_shipping',
        #     field=models.FloatField(blank=True, null=True, verbose_name='\u0441\u0443\u043c\u043c\u0430 \u0437\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0443'),
        # ),
        # migrations.AlterField(
        #     model_name='buyout',
        #     name='sum_buyout',
        #     field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='\u0441\u0443\u043c\u043c\u0430 \u0432\u044b\u043a\u0443\u043f\u0430'),
        # ),
    ]
