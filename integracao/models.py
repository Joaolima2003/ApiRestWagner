from django.db import models

class UsuarioRecebido(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    data_criada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
