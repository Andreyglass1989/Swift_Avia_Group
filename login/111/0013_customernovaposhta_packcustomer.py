# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-14 14:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LK', '0006_auto_20171104_1755'),
        ('login', '0012_auto_20180814_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerNovaPoshta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('address_client', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(10)])),
                ('comment', models.CharField(blank=True, max_length=150, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PackCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('model_number', models.CharField(blank=True, max_length=200, null=True)),
                ('url1', models.CharField(blank=True, max_length=250, null=True)),
                ('url2', models.CharField(blank=True, max_length=250, null=True)),
                ('word_search', models.CharField(blank=True, max_length=150, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('sender', models.CharField(blank=True, max_length=250, null=True)),
                ('company_transporter', models.CharField(blank=True, max_length=250, null=True)),
                ('recipient_our', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_recip', models.CharField(blank=True, max_length=250, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.Customer')),
            ],
        ),
    ]
