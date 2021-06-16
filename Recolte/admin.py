from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Recolte


class RecolteAdmin(ImportExportModelAdmin):
    list_display = ["id", "code_plante", "code_recolte", "num_recolte", "nombre_fruit_recolter", "modifier_le"]


admin.site.register(Recolte, RecolteAdmin)
