from django.db import models
from Plante.models import Plante

class Recolte(models.Model):
    code_plante = models.ForeignKey(Plante, to_field='code_plante', on_delete=models.CASCADE)
    code_recolte = models.CharField(max_length=25, unique=True)
    num_recolte = models.IntegerField()
    nombre_fruit_recolter = models.IntegerField()
    modifier_le = models.DateTimeField()

    def __str__(self):
        return str(self.code_recolte)
