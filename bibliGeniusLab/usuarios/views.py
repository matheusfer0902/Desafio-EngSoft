from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
import re

def usuarios(request):
    if request.method == 'GET':
        return render(request, 'usuarios.html')
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