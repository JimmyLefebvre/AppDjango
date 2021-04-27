from django.contrib import admin
from .models import Base


class BaseAdmin(admin.ModelAdmin):
    list_display = ["id", "code_accession","code_lot_plante", "lieu", "parcelle", "nom_lot", "nombre_plante", "lot_origine", "espece", "graine_objectif", "remarque", "modifier_le"]


admin.site.register(Base, BaseAdmin)


