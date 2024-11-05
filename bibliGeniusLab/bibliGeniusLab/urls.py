
from django.contrib import admin
from django.urls import path, include
from bibliGeniusLab.views import home, homeLogado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('logado/', homeLogado, name='homeLogado'),
    path('usuarios/', include('usuarios.urls')),
    path('livros/', include('livros.urls'))
]
