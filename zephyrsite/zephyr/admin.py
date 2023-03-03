from django.contrib import admin
from import_export.admin import ExportActionMixin
# Register your models here.
from .models import CA
   
admin.site.register(CA)
