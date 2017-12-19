# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
#from LK.models import User
from login.models import UserProfile, Reviews, File_document, CalculatorGroup


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Дополнительная информация'
    raw_id_fields = ['code_clienta'] #

# Define a new User admin
#class UserAdmin(UserAdmin):

    #list_display = ["username", "last_name", "first_name", "email"]

class File_documentAdmin(admin.ModelAdmin):
    list_display = ['document' , 'packid']

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ["reviews_client", "text_reviews",]
    list_filter = ["date_add", ]
    #search_fields = ["reviews_client"]


class UserAdmin(admin.ModelAdmin):
    inlines = (EmployeeInline,)
    list_display = ["username", "code", "full_name", "email"]
    list_filter = ('groups__name',)
    #search_fields = ["radio_set__full_name", "radio_set__code"]

    def code(self, obj):
        try:
            code = obj.userprofile.code_clienta  # Or change this to how you would access the userprofile object - This was assuming that the User, Profile relationship is OneToOne
            return code
        except:
            return ""

    code.short_description = 'Код клиента'


class CalculatorGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(File_document, File_documentAdmin)

admin.site.register(CalculatorGroup, CalculatorGroupAdmin)
admin.site.register(Reviews, ReviewsAdmin)
# admin.site.register(MyUserAdmin)
