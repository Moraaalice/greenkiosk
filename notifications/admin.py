from django.contrib import admin

# Register your models here.
from.models import Notifications
class NotificationsAdmin(admin.ModelAdmin):
    notification = ("message","time","date","customer","identification_number")
    admin.site.register(Notifications)
