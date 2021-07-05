from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Custom


class CustomAdmin(ImportExportModelAdmin):
    list_display = ["id", "code_accession", "nombre_plante", "fruits_recolter", "graine_recolter", "graine_objectif"]


admin.site.register(Custom, CustomAdmin)
