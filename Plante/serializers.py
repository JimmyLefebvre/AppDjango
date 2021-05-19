from rest_framework import serializers
from .models import Plante


class PlanteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Plante
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop('code_plante')
        return Plante.objects.get_or_create(code_plante=code, defaults=defaults)
