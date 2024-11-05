from django.urls import path
from . import views
from estoque.views import adicionar_estoque

urlpatterns = [
    path('cadastro', views.create_livro, name='cadastro'), 
    path('cadastro/estoque/<int:livro_id>/', adicionar_estoque, name='adicionar_estoque'),
    path('livro/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
]