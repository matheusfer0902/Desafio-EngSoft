from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
import re
from livros.models import Livro
from emprestimos.models import Emprestimo

def create_usuarios(request):
    if request.method == 'GET':
        return render(request, 'create_usuarios.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        senha = request.POST.get('senha')
        tipo_usuario = request.POST.get('tipo_usuario')

        usuario = Usuario.objects.filter(email=email)

        if usuario.exists():
            return HttpResponse('email já existe')

        usuario = Usuario(
            nome = nome,
            email = email,
            senha = senha,
            tipo_usuario = tipo_usuario,
            endereco = endereco,
            telefone = telefone,
        )

        usuario.save()

        return redirect('home')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        try:
            usuario = Usuario.objects.get(email=email, senha=senha)
            # Armazena o ID do usuário na sessão
            request.session['usuario_id'] = usuario.id
            request.session['tipo_usuario'] = usuario.tipo_usuario
            return redirect('homeLogado')
        except Usuario.DoesNotExist:
            # Tratar o caso em que o usuário não é encontrado
            return render(request, 'login_usuario.html', {'error': 'Email ou senha inválidos'})
    return render(request, 'login_usuario.html')

def perfil_usuario(request):
    usuario_id = request.session.get('usuario_id')
    
    if not usuario_id:
        # Redireciona para o login se não estiver "logado"
        return redirect('login')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
        emprestimos = Emprestimo.objects.filter(usuario_id=usuario_id)
        
        context = {
            'usuario': usuario,
            'emprestimos': emprestimos
        }
        return render(request, 'perfil_usuario.html', context)
    except Usuario.DoesNotExist:
        return redirect('login')