from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    senha = models.CharField(max_length=255)
    tipo_usuario = models.IntegerField(default=1)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)

    class Meta:
        db_table = 'usuarios'

    def __str__(self) -> str:
        return self.nome

