from django.db import models

class usuario(models.Model):
    login = models.CharField(max_length=20)
    auth = models.CharField(max_length=25)
    nascimento = models.DateField()
    def __str__(self):
        return self.login
