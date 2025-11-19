projetos/test_models.py
from django.test import TestCase
from .models import Participantes 

class ParticipanteModelTest(TestCase):
    def test_criacao_projeto(self):
        projeto = Projeto.objects.create(nome='Novo Website', descricao='Descrição do projeto.')
        self.assertEqual(projeto.nome, 'Novo Website')
    
    def test_str_representation(self):
        projeto = Projeto.objects.create(nome='Nome para Teste Str')
        self.assertEqual(str(projeto), 'Nome para Teste Str')
