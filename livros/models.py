from django.db import models

class Livro(models.Model):

    STATUS = (
        ('QUERO_LER', 'Quero Ler'),
        ('LENDO', 'Lendo'),
        ('CONCLUIDO', 'Concluído'),
        ('ABANDONADO', 'Abandonado'),
    )

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=100)
    ano = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='QUERO_LER'
    )

    progresso = models.IntegerField(default=0)
    nota = models.IntegerField(default=0)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Favorito(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    adicionado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Favoritos"

    def __str__(self):
        return f"Favorito: {self.livro.titulo}"