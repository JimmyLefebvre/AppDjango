from rest_framework import serializers
from .models import Recolte


class RecolteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recolte
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop('code_recolte')
        return Recolte.objects.get_or_create(code_recolte=code, defaults=defaults)
