from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
