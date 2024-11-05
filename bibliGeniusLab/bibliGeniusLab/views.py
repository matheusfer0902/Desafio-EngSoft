from django.shortcuts import render
from livros.models import Livro

def home(request):
    livros_list = Livro.objects.all()
    return render(request, 'home.html', {'livros': livros_list})

def homeLogado(request):
    livros_list = Livro.objects.all()
    return render(request, 'homeLogado.html', {'livros': livros_list})
