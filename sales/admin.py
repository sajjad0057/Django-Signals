from django.contrib import admin
from .models import Sale

# Register your models here.


class SaleAdmin(admin.ModelAdmin):
    fileds = ['order','amount']
    list_display = ['order','amount']

admin.site.register(Sale,SaleAdmin)
