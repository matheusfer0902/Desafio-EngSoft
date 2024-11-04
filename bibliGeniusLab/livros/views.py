from django.shortcuts import render

def create_livro(request):
    if request.method == 'GET':
        return render(request, 'create_livro.html')
