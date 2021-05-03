from django.contrib import admin
from django.urls import path
from Base.views import get_base, base_add, get_lot_graine_extraite
from Plantation.views import get_plantations, plantation_add
from Recolte.views import get_recoltes, recolte_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', get_base),
    path('base_add/', base_add),
    path('plantation/', get_plantations),
    path('plantation_add/', plantation_add),
    path('recolte/', get_recoltes),
    path('recolte_add/', recolte_add),
    path('base/getGraine/<str:code_lot_plante>', get_lot_graine_extraite)
]
