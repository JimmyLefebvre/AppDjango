from rest_framework import serializers
from .models import Piments
from .models import Aubergines
from .models import Tomates
from .models import Melons


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
        return Aubergines.objects.get_or_create(Code_barre_lot=code, defaults=defaults)


class TomatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tomates
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop("Code_barre_lot")
        return Tomates.objects.get_or_create(Code_barre_lot=code, defaults=defaults)

class MelonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Melons
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop("Code_barre_lot")
        return Melons.objects.get_or_create(Code_barre_lot=code, defaults=defaults)
