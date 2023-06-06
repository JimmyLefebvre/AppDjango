from django.db import models


class Piments(models.Model):
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


class Aubergines(models.Model):
    ID = models.IntegerField(primary_key=True, blank=True)
    CodeMM = models.CharField(max_length=150)
    Lot_absent_jete_fini = models.CharField(max_length=20)
    Annee = models.IntegerField()
    Type_de_lot = models.CharField(max_length=150, blank=True, null=True)
    Lieu = models.CharField(max_length=10)
    Remarques = models.CharField(max_length=500, blank=True, null=True)
    Num_plante = models.CharField(max_length=1)
    Pollinisation = models.CharField(max_length=1)
    Quantite = models.IntegerField()
    Parcelle = models.CharField(max_length=50)
    Lot_parent = models.CharField(max_length=150, blank=True, null=True)
    Date_premiere_recolte = models.DateField()
    Nombre_de_fruits_recoltes = models.IntegerField()
    Code_barre_lot = models.CharField(max_length=25, unique=True)
    Long_terme = models.CharField(max_length=50)
    Lot_congele = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Code_barre_lot)


class Tomates (models.Model):
    ID = models.IntegerField(primary_key=True, blank=True)
    IDTO = models.CharField(max_length=150)
    RefLieu = models.CharField(max_length=10)
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
    Test_toBRFV = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.Code_barre_lot)


class Melons (models.Model):
    ID = models.IntegerField(primary_key=True, blank=True)
    IDTO = models.CharField(max_length=150)
    RefLieu = models.CharField(max_length=10)
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
    Test_toBRFV = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return str(self.Code_barre_lot)


# sudo singularity shell  --writable  appmobiledjango_v1.sandbox/
# Singularity> cd /opt/django_database
# Singularity> python3 manage.py makemigrations
# Singularity> python3 manage.py migrate
# Singularity> exit

