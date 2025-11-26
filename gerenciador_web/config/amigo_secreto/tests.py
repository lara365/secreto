from django.test import TestCase
from .models import Grupo
from datetime import date

class GrupoModelTest(TestCase):

    def test_criacao_grupo(self):
        grupo = Grupo.objects.create(
            nome='Amigo Secreto da Família',
            descricao='Grupo criado para o Natal',
            data_sorteio=date(2025, 12, 25),
            valor_limite=100
        )
        self.assertEqual(grupo.nome, 'Amigo Secreto da Família')
        self.assertEqual(grupo.valor_limite, 100)

    def test_str_representation(self):
        grupo = Grupo.objects.create(
            nome='Grupo de Teste',
            descricao='Teste',
            data_sorteio=date(2025, 12, 20),
            valor_limite=50
        )
        self.assertEqual(str(grupo), 'Grupo de Teste')
