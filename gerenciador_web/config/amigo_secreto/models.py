from django.db import models


class Grupo(models.Model):
    nome = models.CharField(max_length=200)
    data_sorteio = models.DateField(blank=True, null=True)
    valor_limite = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome


class Participante(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=50, unique=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='participantes', null=True, blank=True)
    lista_desejos = models.JSONField(default=list)
    resultado = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='quem_tirou')

    def __str__(self):
        return f"{self.nome} ({self.login})"


class Administrador(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='administradores', null=True, blank=True)

    def __str__(self):
        return self.nome


class ListaDesejos(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='listas')
    item = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.participante.nome} - {self.item}"


class Sorteio(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='sorteios')
    quem_tirou = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='quem_tirou_no_grupo')
    amigo = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='foi_tirado_por')

    def __str__(self):
        return f"{self.quem_tirou.nome} → {self.amigo.nome}"