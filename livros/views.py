from django.shortcuts import render
from .models import Livro, Favorito
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    livros = Livro.objects.filter(usuario=request.user)
    
    # Estatísticas
    total_livros = Livro.objects.count()
    livros_lendo = Livro.objects.filter(status='LENDO').count()
    livros_concluidos = Livro.objects.filter(status='CONCLUIDO').count()
    livros_favoritos = Favorito.objects.count()
    
    context = {
        'livros': livros,
        'total_livros': total_livros,
        'livros_lendo': livros_lendo,
        'livros_concluidos': livros_concluidos,
        'livros_favoritos': livros_favoritos,
    }
    return render(request, 'dashboard.html', context)

@login_required
def meus_livros(request):
    # Mostrar todos os livros adicionados
    livros = Livro.objects.all().order_by('-criado_em')
    context = {'livros': livros}
    return render(request, 'meus_livros.html', context)

@login_required
def favoritos(request):
    # Buscar livros marcados como favoritos
    favoritos_obj = Favorito.objects.all().order_by('-adicionado_em')
    favoritos = [fav.livro for fav in favoritos_obj]
    context = {'favoritos': favoritos}
    return render(request, 'favoritos.html', context)

@login_required
def metas(request):
    # TODO: buscar metas do banco de dados
    metas = []
    context = {'metas': metas}
    return render(request, 'metas.html', context)

from django.shortcuts import render, redirect
from .forms import CadastroForm

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