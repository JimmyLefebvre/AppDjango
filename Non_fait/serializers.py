from rest_framework import serializers
from .models import NonFait


class NonFaitSerializers(serializers.ModelSerializer):
    class Meta:
        model = NonFait
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop("code_accession")
        num = defaults.pop("numero_plante")
        return NonFait.objects.get_or_create(code_accession=code, numero_plante=num, defaults=defaults)
