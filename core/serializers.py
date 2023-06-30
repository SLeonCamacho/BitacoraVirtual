from .models import Persona, Ingreso
from rest_framework import routers, serializers, viewsets


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


class IngresoSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    persona = PersonaSerializer()

    class Meta:
        model = Ingreso
        fields = '__all__'
