from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True, db_column='usuario_id')  # Definindo o nome da coluna
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

