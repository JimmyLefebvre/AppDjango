from django.contrib import admin
from django.urls import path, include
from Plantation.views import get_plantation, plantation_add, get_lot_graine_extraite
from Plante.views import get_plante, plante_add
from Recolte.views import get_recoltes, recolte_add
from Graine.views import get_graines, graine_add
from Avancement.views import update_non_fait, update_en_cours
from Access.views import update_plantes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantation/', get_plantation),
    path('plantation_add/', plantation_add),
    path('plante/', get_plante),
    path('plante_add/', plante_add),
    path('recolte/', get_recoltes),
    path('recolte_add/', recolte_add),
    path('plantation/getGraine/<str:code_lot_plante>', get_lot_graine_extraite),
    path('graine/', get_graines),
    path('graine_add/', graine_add),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('graine_add/en_cours/', update_en_cours),
    path('graine_add/en_cours/non_fait/', update_non_fait),
    path('graine_add/en_cours/non_fait/plantes/', update_plantes)
]
