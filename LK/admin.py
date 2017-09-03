from django.contrib import admin
from django.contrib.auth.models import User
from LK.models import Pack, AddressCategory, Customer, PackProduct, CustomerRecipients
# Register your models here.
# Register your models here.

class PackAdmin(admin.ModelAdmin):
    list_display = ["pack_number", "external_id", "customer_id", "pack_status_id", "comment", "date_added"]
    list_filter = ["pack_status_id"]

class PackProductAdmin(admin.ModelAdmin):
    list_display = ["pack_id", "name", "quantity", "weight",]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["external_id", "full_name", ] #"customer_id",
    search_fields = ["external_id", "lastname", "firstname"]


admin.site.register(Pack, PackAdmin)
admin.site.register(AddressCategory)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerRecipients)
admin.site.register(PackProduct, PackProductAdmin)
#admin.site.register(User)
admin.site.site_header = "Swift Avia Group Admin"
#admin.site.register(Air)