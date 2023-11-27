from django.contrib import admin
from.models import CheckItem

# Register your models here.
class CheckItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'listnumber', 'person', 'locations', 'checkList', 'note', 'show_image']
    search_fields = ['listnumber','person']
admin.site.register(CheckItem, CheckItemAdmin)