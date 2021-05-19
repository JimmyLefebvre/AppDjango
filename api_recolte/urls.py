from django.contrib import admin
from django.urls import path, include
from Plantation.views import get_base, base_add, get_lot_graine_extraite
from Plante.views import get_plantations, plantation_add
from Recolte.views import get_recoltes, recolte_add
from Graine.views import get_graines, graine_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', get_base),
    path('base_add/', base_add),
    path('plantation/', get_plantations),
    path('plantation_add/', plantation_add),
    path('recolte/', get_recoltes),
    path('recolte_add/', recolte_add),
    path('base/getGraine/<str:code_lot_plante>', get_lot_graine_extraite),
    path('graine/', get_graines),
    path('graine_add/', graine_add),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
