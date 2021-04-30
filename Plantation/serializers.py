from rest_framework import serializers
from .models import Plantation


class PlantationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plantation
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop('code_lot_plante')
        return Plantation.objects.get_or_create(code_lot_plante=code, defaults=defaults)
