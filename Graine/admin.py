from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Graine


class GraineAdmin(ImportExportModelAdmin):
    list_display = ["id", "code_recolte", "nombre_graine_extraite", "code_graine", "modifier_le"]


admin.site.register(Graine, GraineAdmin)
