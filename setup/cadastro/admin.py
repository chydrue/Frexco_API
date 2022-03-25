from django.contrib import admin
from cadastro.models import usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'login', 'auth', 'nascimento')
    list_display_links = ('id', 'login')
    search_fields = ('login',)

admin.site.register(usuario, Usuarios)