from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages

from .models import Grupo   


class CasosDeBordaViewsTest(TestCase):

    def setUp(self):
        
        self.grupo_existente = Grupo.objects.create(nome="Grupo Existente")

    def test_criar_grupo_valido_cria_objeto(self):
        url = reverse('criar_grupo')
        grupos_antes = Grupo.objects.count()

        response = self.client.post(url, data={
            'nome': 'Novo Grupo',
            'data_sorteio': '2025-10-10',
            'valor_limite': '150'
        })

        
        self.assertEqual(Grupo.objects.count(), grupos_antes + 1)

        
        self.assertRedirects(response, reverse('listar_grupos'))

        
        mensagens = list(get_messages(response.wsgi_request))
        self.assertEqual(str(mensagens[0]), "Grupo criado com sucesso!")

    def test_criar_grupo_sem_nome_nao_cria_objeto(self):
        url = reverse('criar_grupo')
        grupos_antes = Grupo.objects.count()

        response = self.client.post(url, data={
            'nome': '',                   
            'data_sorteio': '2025-10-10',
            'valor_limite': '150'
        })

        
        self.assertEqual(Grupo.objects.count(), grupos_antes)

        
        self.assertRedirects(response, url)

        
        mensagens = list(get_messages(response.wsgi_request))
        self.assertEqual(str(mensagens[0]), "O nome do grupo é obrigatório.")