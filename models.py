from django.db import models


class Plantes(models.Model):
    IDLot = models.IntegerField(primary_key=True, blank=True)
    IDPM = models.IntegerField(blank=True, null=True)
    PM = models.CharField(max_length=150)
    Type_de_lot = models.CharField(max_length=150, blank=True, null=True)
    RefLieu = models.CharField(max_length=50)
    Lieu = models.CharField(max_length=150, blank=True, null=True)
    Parcelle = models.CharField(max_length=50)
    Num_plante = models.CharField(max_length=1)
    Quantite = models.IntegerField()
    Lot_parent = models.CharField(max_length=150, blank=True, null=True)
    Pollinisation = models.CharField(max_length=1)
    Date_premiere_recolte = models.DateField()
    Nombre_de_fruits_recoltes = models.IntegerField()
    Remarques = models.CharField(max_length=500, blank=True, null=True)
    Annee = models.IntegerField()
    Code_barre_lot = models.CharField(max_length=25, unique=True)
    Code_B_du_PP = models.CharField(max_length=150, blank=True, null=True)
    Code_C_du_PP = models.CharField(max_length=150, blank=True, null=True)
    Test_toBRFV = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.Code_barre_lot)

