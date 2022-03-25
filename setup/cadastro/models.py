from django.db import models
from random import choice
import string

def chave():
    tamanho = 15
    valores = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)
    return senha

class usuario(models.Model):
    login = models.CharField(max_length=20)
    auth = models.CharField(max_length=15, default=chave)
    nascimento = models.DateField()
    def __str__(self):
        return self.login
