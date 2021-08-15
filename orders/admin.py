from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    fields = ['cars','name','total','total_price','active']
    list_display = ['name','total','total_price','active']

admin.site.register(Order,OrderAdmin)
