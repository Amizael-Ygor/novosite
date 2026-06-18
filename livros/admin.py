from django.contrib import admin
from .models import Livro, Favorito

admin.site.register(Livro)
admin.site.register(Favorito)