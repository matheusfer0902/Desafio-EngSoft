from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.create_livro, name='cadastro'), 
]