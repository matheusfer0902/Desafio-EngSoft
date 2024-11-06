from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction
from usuarios.models import Usuario
from livros.models import Livro
from .models import Emprestimo
from estoque.models import Estoque

def cadastro_emprestimo(request):
    if request.method == 'GET':
        # Verifique se o usuário está logado e obtenha seu ID
        usuario_logado = request.session.get('usuario_id')  # Supondo que o ID do usuário logado esteja armazenado na sessão
        if not usuario_logado:
            return redirect('login')  # Redireciona para login se o usuário não estiver logado

        livro_list = Livro.objects.all()
        return render(request, 'create_emprestimo.html', {'usuario_id': usuario_logado, 'livros': livro_list})
    
    elif request.method == 'POST':
        # Agora você não precisa obter o usuário do formulário
        usuario_id = request.session.get('usuario_id')
        livro_id = request.POST.get('livro')
        data_emprestimo = request.POST.get('data_empresitmo')
        data_devolucao = request.POST.get('data_devolucao')
        data_devolvido = request.POST.get('data_devolvido')

        # Validação de campos obrigatórios
        if not (usuario_id and livro_id and data_emprestimo and data_devolucao):
            return HttpResponse("Todos os campos obrigatórios devem ser preenchidos.", status=400)

        try:
            with transaction.atomic():
                usuario = Usuario.objects.get(id=usuario_id)
                livro = Livro.objects.get(id=livro_id)
                estoque = Estoque.objects.get(id_livro=livro)

                if estoque.quantidade_disponivel > 0:
                    emprestimo = Emprestimo.objects.create(
                        usuario=usuario,
                        livro=livro,
                        data_emprestimo=data_emprestimo,
                        data_devolucao=data_devolucao,
                        data_devolvido=data_devolvido,
                    )
                    estoque.quantidade_disponivel -= 1
                    estoque.save()
                    return HttpResponse('sucesso_emprestimo')
                else:
                    return HttpResponse("Livro indisponível para empréstimo.", status=400)

        except Usuario.DoesNotExist:
            return HttpResponse("Usuário não encontrado.", status=404)
        except Livro.DoesNotExist:
            return HttpResponse("Livro não encontrado.", status=404)
        except Estoque.DoesNotExist:
            return HttpResponse("Estoque do livro não encontrado.", status=404)
        except Exception as e:
            return HttpResponse(f"Erro: {e}", status=500)
