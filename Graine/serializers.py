from rest_framework import serializers
from .models import Graine


class GraineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Graine
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop('code_recolte')
        return Graine.objects.get_or_create(code_recolte=code, defaults=defaults)
