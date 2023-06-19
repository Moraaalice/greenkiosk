from django.contrib import admin

# Register your models here.
from.models import Order
class Order(admin.ModelAdmin):
    order = ("order_number","order_total","date","location","delivery_options","delivery_date")
    admin.site.register(Order)
