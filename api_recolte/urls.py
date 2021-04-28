from django.contrib import admin
from django.urls import path
from Base.views import get_base, base_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', get_base),
    path('base_add/', base_add)
]
