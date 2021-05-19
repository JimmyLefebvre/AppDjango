from django.contrib import admin
from .models import Plantation


class PlantationAdmin(admin.ModelAdmin):
    list_display = ["id", "code_accession", "code_lot_plante", "lieu", "parcelle", "nom_lot", "nombre_plante",
                    "lot_origine", "espece", "graine_objectif", "remarque", "modifier_le"]


admin.site.register(Plantation, PlantationAdmin)
