from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import PerfilModel

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilModel,
        exclude = ('modified', 'created')

class PerfilCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilModel,
        fields = ('nome_instituicao', 'cep', 'cnpj')