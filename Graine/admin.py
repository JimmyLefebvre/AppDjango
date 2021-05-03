from django.contrib import admin
from .models import Graine


class GraineAdmin(admin.ModelAdmin):
    list_display = ["id", "code_recolte", "nombre_graine_extraite", "code_graine", "modifier_le"]


admin.site.register(Graine, GraineAdmin)
