from django.shortcuts import render, get_object_or_404
from .models import Estoque
from livros.models import Livro
from django.http import HttpResponse

def adicionar_estoque(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'GET':
        return render(request, 'adicionar_estoque.html', {'livro_id': livro_id})
    elif request.method == 'POST':
        quantidade_total = int(request.POST.get('quantidade_total'))

        estoque = Estoque(
            id_livro=livro,
            quantidade_total=quantidade_total,
            quantidade_disponivel=quantidade_total  # Definir quantidade atual como total
        )

        estoque.save()

        return HttpResponse('Estoque cadastrado com sucesso.')
