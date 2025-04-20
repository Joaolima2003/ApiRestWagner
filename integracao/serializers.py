from .models import UsuarioRecebido
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password

class UsuarioRecebidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRecebido
        fields = ['id', 'nome', 'email', 'senha', 'data_criada']


    def create(self, validated_data):
        validated_data['senha'] = make_password(validated_data['senha'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'senha' in validated_data:
            validated_data['senha'] = make_password(validated_data['senha'])
        return super().update(instance, validated_data)   