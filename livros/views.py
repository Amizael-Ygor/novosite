from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def meus_livros(request):
    # TODO: buscar livros do banco de dados
    livros = []
    context = {'livros': livros}
    return render(request, 'meus_livros.html', context)

def favoritos(request):
    # TODO: buscar livros favoritos do banco de dados
    favoritos = []
    context = {'favoritos': favoritos}
    return render(request, 'favoritos.html', context)

def metas(request):
    # TODO: buscar metas do banco de dados
    metas = []
    context = {'metas': metas}
    return render(request, 'metas.html', context)