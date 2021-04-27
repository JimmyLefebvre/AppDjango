from django.contrib import admin
from django.urls import path
from Base.views import get_base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', get_base),
]
