from rest_framework import serializers
from .models import Plantation


class PlantationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Plantation
        fields = ("code_accession", "code_lot_plante", "lieu", "parcelle", "nom_lot", "nombre_plante", "lot_origine", "espece", "graine_objectif", "remarque", "modifier_le")

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop('code_lot_plante')
        return Plantation.objects.get_or_create(code_lot_plante=code, defaults=defaults)
