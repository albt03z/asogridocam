from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'phone_number', 'country', 'message']
    search_fields = ['name', 'surname', 'email', 'phone_number', 'country', 'message']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'alpha2_code', 'alpha3_code', 'flag']
    search_fields = ['name', 'alpha2_code', 'alpha3_code', 'flag']

@admin.register(Ally)
class AllyAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'website')
    list_editable = ('order',)
    search_fields = ('name',)