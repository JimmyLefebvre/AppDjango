from django.db import models
from Recolte.models import Recolte


class Graine(models.Model):
    code_recolte = models.OneToOneField(Recolte, to_field='code_recolte', on_delete=models.CASCADE, unique=True)
    nombre_graine_extraite = models.IntegerField()
    modifier_le = models.DateTimeField()

    def __str__(self):
        return str(self.code_recolte)
