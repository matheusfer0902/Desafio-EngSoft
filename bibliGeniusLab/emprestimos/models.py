from django.db import models
from livros.models import Livro
from usuarios.models import Usuario

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    data_devolvido = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'emprestimo'
