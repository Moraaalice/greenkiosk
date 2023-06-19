from django.contrib import admin

# Register your models here.
from .models import Vendor
class Vendor(admin.ModelAdmin):
    vendor = ("name","location","contact","store_name","user_name")
    admin.site.register(Vendor)