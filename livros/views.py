from django.shortcuts import render, redirect
from .forms import CadastroForm

def dashboard(request):
    return render(request, 'dashboard.html')

def meus_livros(request):
    return render(request, 'meus_livros.html')

def favoritos(request):
    return render(request, 'favoritos.html')

def metas(request):
    return render(request, 'metas.html')

def cadastro(request):

    form = CadastroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/accounts/login/')

    return render(
        request,
        'cadastro.html',
        {'form': form}
    )