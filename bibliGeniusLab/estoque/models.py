from django.db import models
from livros.models import Livro

class Estoque(models.Model):
    id_livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name='estoques',
        db_column='id_livro',
        primary_key=True
    )
    quantidade_total = models.PositiveIntegerField(default=0)
    quantidade_disponivel = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.quantidade_atual = self.quantidade_total
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'estoque'