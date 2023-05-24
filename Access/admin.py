from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Piments, Aubergines, Tomates


class PimentsAdmin(ImportExportModelAdmin):
    list_display = ["IDLot", "IDPM", "PM", "Type_de_lot", "RefLieu", "Lieu", "Parcelle", "Num_plante", "Quantite",
                    "Lot_parent", "Pollinisation", "Date_premiere_recolte", "Nombre_de_fruits_recoltes", "Remarques",
                    "Annee", "Code_barre_lot", "Code_B_du_PP", "Code_C_du_PP", "Test_toBRFV"]


class AuberginesAdmin(ImportExportModelAdmin):
    list_display = ["ID", "CodeMM", "Lot_absent_jete_fini", "Annee", "Type_de_lot", "Lieu", "Remarques", "Num_plante", "Pollinisation", "Quantite", "Parcelle", "Lot_parent", "Date_premiere_recolte", "Nombre_de_fruits_recoltes", "Code_barre_lot", "Long_terme", "Lot_congele"]

class TomatesAdmin(ImportExportModelAdmin):
    list_display = ["ID", "IDTO", "RefLieu", "Lieu", "Parcelle", "Num_plante", "Quantite", "Lot_parent", "Pollinisation", "Date_premiere_recolte", "Nombre_de_fruits_recoltes", "Remarques", "Annee", "Code_barre_lot", "Test_toBRFV"]


admin.site.register(Piments, PimentsAdmin)
admin.site.register(Aubergines, AuberginesAdmin)
admin.site.register(Tomates, TomatesAdmin)
