from rest_framework import viewsets
from cadastro.models import usuario
from cadastro.serializer import usuarioSerializer
from rest_framework import filters, generics
from django.shortcuts import render


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'login']


def index(request):
    return render(request, "index.html")