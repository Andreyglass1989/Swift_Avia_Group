from django.contrib import admin
from django.contrib.auth.models import User
from LK.models import Customer, Pack, PackProduct

#from import_export import resources

#from import_export.admin import ImportExportModelAdmin
#from import_export import fields
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["external_id", "full_name", ] #"customer_id",
    search_fields = ["external_id", "lastname", "firstname"]

# class PackResource(resources.ModelResource):
#     quantity = fields.Field(column_name='quantity')
#     name = fields.Field(column_name='name')
#     class Meta:
#         model = Pack
#         fields = ('pack_number', 'name', 'quantity', 'total', 'weight')
#         export_order = ('pack_number', 'name', 'quantity', 'total', 'weight')

class PackProductInline(admin.TabularInline):
    model = PackProduct
    exclude = []


class PackAdmin(admin.ModelAdmin):#(ImportExportModelAdmin):
    #resource_class = PackResource
    #date_hierarchy = 'date_added'
    search_fields = ["pack_number"]
    inlines = (PackProductInline,)
    raw_id_fields = ['customer']
    list_filter = ['pack_status']
    list_display = ["pack_number", "date_added", "weight", ]



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Pack, PackAdmin)
#admin.site.register(User)
admin.site.site_header = "Swift Avia Group Admin"
