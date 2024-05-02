from django.contrib import admin

from business_api import models
from import_export.admin import ExportActionMixin
from rest_framework.authtoken.models import Token

# Register your models here.

class CashBackAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['user_id', 'user_number', 'amount']


admin.site.register(models.CustomUser)
admin.site.register(models.CashBack, CashBackAdmin)

