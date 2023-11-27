from django.contrib import admin
from.models import Itemname, ListNumber, NumberList, Person, Locations, CheckList

# Register your models here.
class ItemnameAdmin(admin.ModelAdmin):
    list_display = ['id','list']
admin.site.register(Itemname, ItemnameAdmin)

class NumberListAdmin(admin.ModelAdmin):
    list_display = ['id','unit', 'type_1', 'type_2', 'type_3', 'degree']
admin.site.register(NumberList, NumberListAdmin)

class ListNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'list','unit', 'type_1', 'type_2', 'type_3', 'degree']
admin.site.register(ListNumber, ListNumberAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Person, PersonAdmin)

class LocationsAdmin(admin.ModelAdmin):
    list_display = ['id','location']
admin.site.register(Locations, LocationsAdmin)

class CheckListAdmin(admin.ModelAdmin):
    list_display = ['id', 'check_list']
admin.site.register(CheckList, CheckListAdmin)