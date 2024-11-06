from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.create_usuarios, name='cadastro_user'),  # Rota para cadastro
    path('login', views.login_view, name='login'),      # Rota para login
    path('', views.login_view, name='login_redirect'),  # Rota principal para /usuarios
    path('perfil', views.perfil_usuario, name='perfil_usuario'),  # Rota para a página de perfil do usuário
]
