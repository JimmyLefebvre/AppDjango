from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Plantes


class PlantesAdmin(ImportExportModelAdmin):
    list_display = ["IDLot", "IDPM", "PM", "Type_de_lot", "RefLieu", "Lieu", "Parcelle", "Num_plante", "Quantite",
                    "Lot_parent", "Pollinisation", "Date_premiere_recolte", "Nombre_de_fruits_recoltes", "Remarques",
                    "Annee", "Code_barre_lot", "Code_B_du_PP", "Code_C_du_PP", "Test_toBRFV"]


admin.site.register(Plantes, PlantesAdmin)
