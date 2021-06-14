import datetime

from django.db import models

def default_datetime():
    now = datetime.datetime.now()
    now.replace(microsecond=0)
    return now


class Plantation(models.Model):
    code_accession = models.CharField(max_length=150)
    code_lot_plante = models.CharField(max_length=16, unique=True)
    lieu = models.CharField(max_length=10)
    parcelle = models.CharField(max_length=5)
    nom_lot = models.CharField(max_length=150, blank=True)
    nombre_plante = models.IntegerField()
    lot_origine = models.CharField(max_length=150, blank=True)
    espece = models.CharField(max_length=150, blank=True)
    graine_objectif = models.IntegerField()
    remarque = models.CharField(max_length=500, blank=True)
    modifier_le = models.DateTimeField(db_index=True, auto_now=True)

    def __str__(self):
        return str(self.code_lot_plante)
