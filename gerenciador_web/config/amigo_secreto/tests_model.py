from django.test import TestCase
from .models import Grupo, Participante, Administrador, ListaDesejos, Sorteio


class GrupoModelTest(TestCase):
    def test_criacao_grupo(self):
        grupo = Grupo.objects.create(nome='Grupo Teste')
        self.assertEqual(grupo.nome, 'Grupo Teste')

    def test_str_representation(self):
        grupo = Grupo.objects.create(nome='Grupo Exemplo')
        self.assertEqual(str(grupo), 'Grupo Exemplo')


class ParticipanteModelTest(TestCase):
    def test_criacao_participante(self):
        participante = Participante.objects.create(
            nome='João Silva',
            login='joao123'
        )
        self.assertEqual(participante.nome, 'João Silva')
        self.assertEqual(participante.login, 'joao123')

    def test_str_representation(self):
        participante = Participante.objects.create(
            nome='Maria',
            login='maria01'
        )
        self.assertEqual(str(participante), 'Maria (maria01)')


class AdministradorModelTest(TestCase):
    def test_criacao_administrador(self):
        admin = Administrador.objects.create(
            nome='Carlos Admin',
            email='carlos@teste.com'
        )
        self.assertEqual(admin.nome, 'Carlos Admin')
        self.assertEqual(admin.email, 'carlos@teste.com')

    def test_str_representation(self):
        admin = Administrador.objects.create(
            nome='Luciana',
            email='luciana@teste.com'
        )
        self.assertEqual(str(admin), 'Luciana')


class ListaDesejosModelTest(TestCase):
    def test_criacao_lista_desejos(self):
        participante = Participante.objects.create(
            nome='Bruno',
            login='bruno12'
        )
        lista = ListaDesejos.objects.create(
            participante=participante,
            item='Livro de Python'
        )
        self.assertEqual(lista.item, 'Livro de Python')
        self.assertEqual(lista.participante.nome, 'Bruno')

    def test_str_representation(self):
        participante = Participante.objects.create(
            nome='Ana',
            login='ana45'
        )
        lista = ListaDesejos.objects.create(
            participante=participante,
            item='Headphone'
        )
        self.assertEqual(str(lista), 'Ana - Headphone')


class SorteioModelTest(TestCase):
    def test_criacao_sorteio(self):
        grupo = Grupo.objects.create(nome='Grupo Beta')
        p1 = Participante.objects.create(nome='João', login='joao1')
        p2 = Participante.objects.create(nome='Maria', login='maria1')

        sorteio = Sorteio.objects.create(
            grupo=grupo,
            quem_tirou=p1,
            amigo=p2
        )

        self.assertEqual(sorteio.grupo.nome, 'Grupo Beta')
        self.assertEqual(sorteio.quem_tirou.nome, 'João')
        self.assertEqual(sorteio.amigo.nome, 'Maria')

    def test_str_representation(self):
        grupo = Grupo.objects.create(nome='Grupo Teste')
        p1 = Participante.objects.create(nome='Carlos', login='carlos1')
        p2 = Participante.objects.create(nome='Pedro', login='pedro2')

        sorteio = Sorteio.objects.create(
            grupo=grupo,
            quem_tirou=p1,
            amigo=p2
        )

        self.assertEqual(str(sorteio), 'Carlos → Pedro')
