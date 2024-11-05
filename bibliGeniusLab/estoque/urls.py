from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/<int:livro_id>/', views.adicionar_estoque, name='adicionar_estoque'),
]