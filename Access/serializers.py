from rest_framework import serializers
from .models import Piments
from .models import Aubergines


class PimentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Piments
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop("Code_barre_lot")
        return Piments.objects.get_or_create(Code_barre_lot=code, defaults=defaults)


class AuberginesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aubergines
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop("Code_barre_lot")
        return Piments.objects.get_or_create(Code_barre_lot=code, defaults=defaults)
