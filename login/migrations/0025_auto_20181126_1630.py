# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-11-26 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0024_buyout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_document',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='file_document',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='file_document',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='file_document',
            name='image5',
        ),
        migrations.AddField(
            model_name='buyout',
            name='sum_buyout',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='buyout',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buyout',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='buyout',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buyout',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buyout',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='buyout',
            name='status',
            field=models.CharField(choices=[('\u0421\u043e\u0437\u0434\u0430\u043d', '\u0421\u043e\u0437\u0434\u0430\u043d'), ('\u041e\u043f\u043b\u0430\u0447\u0435\u043d', '\u041e\u043f\u043b\u0430\u0447\u0435\u043d'), ('\u0412\u044b\u043a\u0443\u043f\u043b\u0435\u043d\u043e', '\u0412\u044b\u043a\u0443\u043f\u043b\u0435\u043d\u043e'), ('\u041e\u0436\u0438\u0434\u0430\u0435\u0442\u044c\u0441\u044f \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435', '\u041e\u0436\u0438\u0434\u0430\u0435\u0442\u044c\u0441\u044f \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435'), ('\u0414\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u043d\u0430 \u0441\u043a\u043b\u0430\u0434', '\u0414\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d \u043d\u0430 \u0441\u043a\u043b\u0430\u0434'), ('\u041b\u0435\u0442\u0438\u0442 \u0432 \u0423\u043a\u0440\u0430\u0438\u043d\u0443', '\u041b\u0435\u0442\u0438\u0442 \u0432 \u0423\u043a\u0440\u0430\u0438\u043d\u0443'), ('\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u043a\u043b\u0438\u0435\u043d\u0442\u0443', '\u041e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u043a\u043b\u0438\u0435\u043d\u0442\u0443'), ('\u041d\u0435\u0442 \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438', '\u041d\u0435\u0442 \u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438')], default='\u0421\u043e\u0437\u0434\u0430\u043d', max_length=50),
        ),
        migrations.AlterField(
            model_name='file_document',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='lossinair',
            name='comment',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lossinair',
            name='name_tovar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.PackProduct'),
        ),
        migrations.AlterField(
            model_name='lossinair',
            name='plomba_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LK.PlombaDimension'),
        ),
    ]
