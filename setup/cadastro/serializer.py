from rest_framework import serializers
from cadastro.models import usuario

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ['id', 'login', 'auth', 'nascimento']
