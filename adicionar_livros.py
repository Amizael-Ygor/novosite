import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'novosite.settings')
django.setup()

from livros.models import Livro

# Livros de exemplo
livros_exemplo = [
    {
        'titulo': '1984',
        'autor': 'George Orwell',
        'genero': 'Ficção Científica',
        'ano': 1949,
        'status': 'QUERO_LER'
    },
    {
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'genero': 'Romance',
        'ano': 1899,
        'status': 'LENDO'
    },
    {
        'titulo': 'O Hobbit',
        'autor': 'J.R.R. Tolkien',
        'genero': 'Fantasia',
        'ano': 1937,
        'status': 'QUERO_LER'
    },
    {
        'titulo': 'Cem Anos de Solidão',
        'autor': 'Gabriel García Márquez',
        'genero': 'Realismo Mágico',
        'ano': 1967,
        'status': 'CONCLUIDO'
    },
    {
        'titulo': 'O Cortiço',
        'autor': 'Aluísio Azevedo',
        'genero': 'Naturalismo',
        'ano': 1890,
        'status': 'QUERO_LER'
    },
    {
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling',
        'genero': 'Fantasia',
        'ano': 1997,
        'status': 'LENDO'
    },
    {
        'titulo': 'O Senhor dos Anéis: A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien',
        'genero': 'Fantasia',
        'ano': 1954,
        'status': 'CONCLUIDO'
    },
    {
        'titulo': 'Orgulho e Preconceito',
        'autor': 'Jane Austen',
        'genero': 'Romance',
        'ano': 1813,
        'status': 'QUERO_LER'
    },
]

# Adicionar livros
for livro_data in livros_exemplo:
    livro, created = Livro.objects.get_or_create(**livro_data)
    if created:
        print(f"✓ Livro adicionado: {livro.titulo}")
    else:
        print(f"- Livro já existe: {livro.titulo}")

print(f"\nTotal de livros no banco de dados: {Livro.objects.count()}")
