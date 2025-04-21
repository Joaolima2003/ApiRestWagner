from django.db import models

class UsuarioRecebido(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.email
