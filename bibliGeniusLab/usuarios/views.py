from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
import re

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

        return HttpResponse('Usuario Cadastrado')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login_usuario.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        email_usuario = Usuario.objects.filter(email=email)
        senha_usuario = Usuario.objects.filter(senha=senha)

        if email_usuario.exists() and senha_usuario.exists():
            return HttpResponse('logado')
        else:
            return render(request, 'login_usuario.html')