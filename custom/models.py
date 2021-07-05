# SELECT Plantation_plantation.code_accession, Plantation_plantation.nombre_plante, COALESCE(SUM(Recolte_recolte.nombre_fruit_recolter),0) AS total_fruits, COALESCE(SUM(Graine_graine.nombre_graine_extraite),0) as total_graine, Plantation_plantation.graine_objectif
# FROM Plantation_plantation LEFT OUTER JOIN Plante_plante ON Plantation_plantation.code_lot_plante = Plante_plante.code_lot_plante_id
# LEFT OUTER JOIN Recolte_recolte ON Plante_plante.code_plante = Recolte_recolte.code_plante_id LEFT OUTER JOIN Graine_graine ON
# Recolte_recolte.code_recolte = Graine_graine.code_recolte_id
# GROUP BY Plantation_plantation.code_accession;

from django.db import models

class Custom(models.Model):
    code_accession = models.CharField(max_length=150, unique=True)
    nombre_plante = models.IntegerField()
    fruits_recolter = models.IntegerField()
    graine_recolter = models.IntegerField()
    graine_objectif = models.IntegerField()

    def __str__(self):
        return str(self.code_accession)
