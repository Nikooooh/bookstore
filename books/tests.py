from django.test import TestCase
from .models import Livro

class LivroTestCase(TestCase):
    def setUp(self):
        Livro.objects.create(
            titulo='Livro de Teste',
            autor='Autor do Teste',
            descricao='Descrição do Livro de Teste'
        )

    def test_livro_str(self):
        livro = Livro.objects.get(titulo='Livro de Teste')
        self.assertEqual(str(livro), 'Livro de Teste')
