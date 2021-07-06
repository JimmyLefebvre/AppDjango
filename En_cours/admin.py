from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import EnCours


class EnCoursAdmin(ImportExportModelAdmin):
    list_display = ["id", "code_accession", "numero_plante", "nombre_plante", "lieu_parcelle", "fruits_recoltes_plante",
                    "graines_recoltees_plante", "graines_objectif_accession"]


admin.site.register(EnCours, EnCoursAdmin)