from django.contrib import admin

# Register your models here.
from.models import Payments
class PaymentsAdmin(admin.ModelAdmin):
    payment = ("amount","date","receipt","status","order","payment_method")
    admin.site.register(Payments)
