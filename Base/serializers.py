from rest_framework import serializers
from .models import Base

class BaseSerializers(serializers.ModelSerializer):
    modifier_le = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        fields = '__all__'
        model = Base