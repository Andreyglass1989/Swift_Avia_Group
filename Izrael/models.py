# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class IzraelDataForPacking(models.Model):
	box_number = models.IntegerField()
	full_customer_name = models.CharField(max_length=100)
	telephone_number = models.CharField(max_length=100)
	oblast = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	post_number = models.CharField(max_length=30)
	street_home = models.CharField(max_length=255)
	height = models.FloatField()
	description = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.description