from django.contrib import admin
from .models import Menu, Reservation

class MenuAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Reservation)
