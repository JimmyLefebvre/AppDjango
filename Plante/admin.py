from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Plante


class PlanteAdmin(ImportExportModelAdmin):
    list_display = ["id", "code_lot_plante", "num_plante", "type_fecondation", "code_plante", "modifier_le"]


admin.site.register(Plante, PlanteAdmin)
