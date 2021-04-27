from django.db import models
from Base.models import Base


class Plantation(models.Model):
    code_lot_plante = models.ForeignKey(Base, to_field='code_lot_plante', on_delete=models.CASCADE)
    num_plante = models.CharField(max_length=1)
    type_fecondation = models.CharField(max_length=1)
    code_plante = models.CharField(max_length=25, unique=True)
    modifier_le = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.code_plante)
