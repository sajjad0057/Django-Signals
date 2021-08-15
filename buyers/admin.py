from django.contrib import admin
from .models import Buyer

# Register your models here.

class BuyerAdmin(admin.ModelAdmin):
    fields = ['user','from_signal']
    list_display = ('user','from_signal')


admin.site.register(Buyer,BuyerAdmin)