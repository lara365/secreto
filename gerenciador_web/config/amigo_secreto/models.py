from django.db import models

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=50, unique=True)
    lista_desejos = models.JSONField(default=list)  
    resultado = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='quem_tirou'
    )

    def __str__(self):
        return f"Participante: {self.nome} - Resultado: {self.resultado.nome if self.resultado else 'Não sorteado'}"

class Administrador(models.Model):

    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    grupo = models.CharField(max_length=200)  
    valor_presente = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    data_sorteio = models.DateField(blank=True, null=True)
    participantes = models.TextField(blank=True, null=True)  

    
    def __str__(self):
        return self.nome
