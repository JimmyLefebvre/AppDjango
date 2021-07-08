from django.db import models


class EnCours(models.Model):
    code_accession = models.CharField(max_length=150)
    numero_plante = models.CharField(max_length=1)
    nombre_plante = models.IntegerField()
    num_lieu_parcelle = models.CharField(max_length=20, unique=True)
    fruits_recoltes_plante = models.IntegerField()
    graines_recoltees_plante = models.IntegerField()
    graines_objectif_accession = models.IntegerField()

    def __str__(self):
        return str(self.num_lieu_parcelle)


class NonFait(models.Model):
    code_accession = models.CharField(max_length=150)
    numero_plante = models.CharField(max_length=1)
    nombre_plante = models.IntegerField()
    num_lieu_parcelle = models.CharField(max_length=20, unique=True)
    fruits_recoltes_plante = models.IntegerField()
    graines_recoltees_plante = models.IntegerField()
    graines_objectif_accession = models.IntegerField()

    def __str__(self):
        return str(self.num_lieu_parcelle)
