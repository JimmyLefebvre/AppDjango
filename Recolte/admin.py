from django.contrib import admin
from .models import Recolte

class RecolteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recolte._meta.get_fields()]

admin.site.register(Recolte, RecolteAdmin)
