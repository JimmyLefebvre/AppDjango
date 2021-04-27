from django.db import models
from Plantation.models import Plantation

class Recolte(models.Model):
    code_plante = models.ForeignKey(Plantation, to_field='code_plante', on_delete=models.CASCADE)
    num_recolte = models.IntegerField()
    nombre_fruit_recolter = models.IntegerField()
    date_recolte = models.DateTimeField(auto_now_add=True)
    modifier_le = models.DateTimeField(auto_now=True)
