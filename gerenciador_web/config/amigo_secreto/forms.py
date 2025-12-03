# amigo_secreto/forms.py
from django import forms
from .models import Grupo, Participante, ListaDesejos

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'data_sorteio', 'valor_limite']
        widgets = {
            'data_sorteio': forms.DateInput(attrs={'type': 'date'}),
        }

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nome', 'login']
        # O campo 'grupo' não entra aqui pois é preenchido automaticamente pela view

class ListaDesejosForm(forms.ModelForm):
    class Meta:
        model = ListaDesejos
        fields = ['item']
        # O campo 'participante' é preenchido automaticamente pela view