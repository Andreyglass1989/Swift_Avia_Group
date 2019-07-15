from django.contrib import admin

# Register your models here.

from Izrael.models import IzraelDataForPacking


class IzraelDataForPackingAdmin(admin.ModelAdmin):
	list_display = ["box_number", "full_customer_name", "telephone_number", "description"]


# admin.site.register(IzraelDataForPacking, IzraelDataForPackingAdmin)