from django.contrib import admin
from .models import Plante


class PlanteAdmin(admin.ModelAdmin):
    list_display = ["id", "code_lot_plante", "num_plante", "type_fecondation", "code_plante", "modifier_le"]


admin.site.register(Plante, PlanteAdmin)
