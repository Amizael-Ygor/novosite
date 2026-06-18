from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('meus-livros/', views.meus_livros, name='meus_livros'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('metas/', views.metas, name='metas'),
    path('cadastro/', views.cadastro, name='cadastro'),
]