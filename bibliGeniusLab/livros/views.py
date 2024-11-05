from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Livro

def create_livro(request):
    if request.method == 'GET':
        return render(request, 'create_livro.html')
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        isbn = request.POST.get('isbn')
        editora = request.POST.get('editora')
        data_publicacao = request.POST.get('data_publicacao')
        genero = request.POST.get('genero')
        descricao = request.POST.get('descricao')

        livro = Livro(
            titulo = titulo,
            autor = autor,
            isbn = isbn,
            editora = editora,
            data_publicacao = data_publicacao,
            genero = genero,
            descricao = descricao,
        )

        livro.save()

        return redirect('adicionar_estoque', livro_id=livro.id)
