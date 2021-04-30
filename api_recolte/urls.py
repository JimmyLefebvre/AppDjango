from django.contrib import admin
from django.urls import path
from Base.views import get_base, base_add
from Plantation.views import get_plantations,plantation_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', get_base),
    path('base_add/', base_add),
    path('plantation/', get_plantations),
    path('plantation_add/', plantation_add)
]
