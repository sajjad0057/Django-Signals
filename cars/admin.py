from django.contrib import admin
from .models import Car

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    fields = ['buyer','name','price','code']
    list_display = ('buyer','name','price','code')


admin.site.register(Car,CarAdmin)