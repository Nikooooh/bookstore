from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Livro

class LivroViewSetTests(APITestCase):

    def setUp(self):
        self.livro_data = {'titulo': 'Test Book', 'autor': 'Author Test', 'descricao': 'Description Test'}
        self.livro = Livro.objects.create(**self.livro_data)
        self.list_url = reverse('livro-list')
        self.detail_url = reverse('livro-detail', args=[self.livro.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {'titulo': 'New Book', 'autor': 'New Author', 'descricao': 'New Description'}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Livro.objects.count(), 2)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], self.livro_data['titulo'])

    def test_update_book(self):
        updated_data = {'titulo': 'Updated Book', 'autor': 'Updated Author', 'descricao': 'Updated Description'}
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.livro.refresh_from_db()
        self.assertEqual(self.livro.titulo, updated_data['titulo'])

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Livro.objects.count(), 0)
