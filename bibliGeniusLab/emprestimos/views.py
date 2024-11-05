from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction
from usuarios.models import Usuario
from livros.models import Livro
from .models import Emprestimo
from estoque.models import Estoque  # Importando o modelo Estoque

def cadastro_emprestimo(request):
    if request.method == 'GET':
        usuario_list = Usuario.objects.all()
        livro_list = Livro.objects.all()
        return render(request, 'create_emprestimo.html', {'usuarios': usuario_list, 'livros': livro_list})
    
    elif request.method == 'POST':
        # Captura os dados do formulário
        usuario_id = request.POST.get('usuario')
        livro_id = request.POST.get('livro')
        data_emprestimo = request.POST.get('data_empresitmo')
        data_devolucao = request.POST.get('data_devolucao')
        data_devolvido = request.POST.get('data_devolvido')

        # Validando os campos obrigatórios
        if not (usuario_id and livro_id and data_emprestimo and data_devolucao):
            return HttpResponse("Todos os campos obrigatórios devem ser preenchidos.", status=400)

        try:
            with transaction.atomic():  # Inicia uma transação para garantir a consistência dos dados
                # Obtendo o usuário e o livro selecionados
                usuario = Usuario.objects.get(id=usuario_id)
                livro = Livro.objects.get(id=livro_id)
                
                # Obtendo o estoque do livro
                estoque = Estoque.objects.get(id_livro=livro)

                # Verificando se há quantidade disponível em estoque
                if estoque.quantidade_disponivel > 0:
                    # Criando o novo registro de empréstimo
                    emprestimo = Emprestimo.objects.create(
                        usuario=usuario,
                        livro=livro,
                        data_emprestimo=data_emprestimo,
                        data_devolucao=data_devolucao,
                        data_devolvido=data_devolvido,
                    )

                    # Diminuindo a quantidade disponível do livro em 1 no estoque
                    estoque.quantidade_disponivel -= 1
                    estoque.save()

                    # Redirecionando para uma página de sucesso ou outro local após o cadastro
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
