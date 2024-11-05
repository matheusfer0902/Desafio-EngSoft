from django.urls import path
from . import views
from estoque.views import adicionar_estoque

urlpatterns = [
    path('cadastro', views.create_livro, name='cadastro'), 
    path('cadastro/estoque/<int:livro_id>/', adicionar_estoque, name='adicionar_estoque'),  # Rota para o formulário de quantidade
]