from rest_framework import serializers
from .models import Custom

class CustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop('code_accession')
        return Custom.objects.get_or_create(code_accession=code, defaults=defaults)