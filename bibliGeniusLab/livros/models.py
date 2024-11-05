from django.db import models

class Livro(models.Model):
    id = models.AutoField(primary_key=True, db_column='livro_id') 
    titulo = models.CharField(max_length=255)
    autor= models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    editora = models.CharField(default=1)
    data_publicacao = models.DateField()
    genero = models.CharField(max_length=255)
    descricao = models.CharField(max_length=500)

    class Meta:
        db_table = 'livros'

    def __str__(self) -> str:
        return self.titulo
