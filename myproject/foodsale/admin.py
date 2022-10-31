from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import foodsale
    
@admin.register(foodsale)
class foodsaleAdmin(ImportExportModelAdmin):
    pass
        