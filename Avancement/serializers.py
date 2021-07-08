from rest_framework import serializers
from .models import NonFait
from .models import EnCours


class NonFaitSerializers(serializers.ModelSerializer):
    class Meta:
        model = NonFait
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop("num_lieu_parcelle")
        return NonFait.objects.get_or_create(num_lieu_parcelle=code, defaults=defaults)


class EnCoursSerializers(serializers.ModelSerializer):
    class Meta:
        model = EnCours
        fields = "__all__"

    def get_or_create(self):
        defaults = self.validated_data.copy()
        code = defaults.pop("num_lieu_parcelle")
        return EnCours.objects.get_or_create(num_lieu_parcelle=code, defaults=defaults)
