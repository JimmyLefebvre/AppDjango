from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import NonFait
from .models import EnCours


class NonFaitAdmin(ImportExportModelAdmin):
    list_display = ["id", "code_accession", "numero_plante", "nombre_plante", "num_lieu_parcelle",
                    "fruits_recoltes_plante",
                    "graines_recoltees_plante", "graines_objectif_accession"]


class EnCoursAdmin(ImportExportModelAdmin):
    list_display = ["id", "code_accession", "numero_plante", "nombre_plante", "num_lieu_parcelle",
                    "fruits_recoltes_plante", "graines_recoltees_plante", "graines_objectif_accession"]


admin.site.register(NonFait, NonFaitAdmin)

admin.site.register(EnCours, EnCoursAdmin)
