from django.contrib import admin
from .models import Recolte


class RecolteAdmin(admin.ModelAdmin):
    list_display = ["id", "code_plante", "code_recolte", "num_recolte", "nombre_fruit_recolter", "modifier_le"]


admin.site.register(Recolte, RecolteAdmin)
