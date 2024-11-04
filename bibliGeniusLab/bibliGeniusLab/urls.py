
from django.contrib import admin
from django.urls import path, include
from bibliGeniusLab.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('livros/', include('livros.urls'))
]
