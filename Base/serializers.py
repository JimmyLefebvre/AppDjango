from rest_framework import serializers
from .models import Base


class BaseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Base
        fields = ("code_accession", "code_lot_plante", "lieu", "parcelle", "nom_lot", "nombre_plante", "lot_origine", "espece", "graine_objectif", "remarque", "modifier_le")

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop('code_lot_plante')
        return Base.objects.get_or_create(code_lot_plante=code, defaults=defaults)
