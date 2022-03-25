from rest_framework import viewsets
from cadastro.models import usuario
from cadastro.serializer import usuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer

