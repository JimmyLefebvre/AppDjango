from rest_framework import serializers
from .models import Plantes


class PlantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plantes
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop("Code_barre_lot")
        return Plantes.objects.get_or_create(Code_barre_lot=code, defaults=defaults)
