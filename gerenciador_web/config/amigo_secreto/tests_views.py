from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from .models import Grupo, Participante, ListaDesejos, Sorteio
from .forms import GrupoForm, ParticipanteForm, ListaDesejosForm
import random


def listar_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, "grupos/listar_grupos.html", {"grupos": grupos})


def criar_grupo(request):
    if request.method == "POST":
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_grupos")
    else:
        form = GrupoForm()
    return render(request, "grupos/form_grupo.html", {"form": form})


def entrar_no_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    if request.method == "POST":
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.grupo = grupo
            participante.save()
            return redirect("detalhe_grupo", grupo_id=grupo.id)
    else:
        form = ParticipanteForm()
    return render(request, "participantes/entrar_no_grupo.html", {"form": form, "grupo": grupo})


def cadastrar_lista_desejos(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    if request.method == "POST":
        form = ListaDesejosForm(request.POST)
        if form.is_valid():
            lista = form.save(commit=False)
            lista.participante = participante
            lista.save()
            return redirect("detalhe_grupo", grupo_id=participante.grupo.id)
    else:
        form = ListaDesejosForm()
    return render(request, "desejos/form_lista_desejos.html", {"form": form, "participante": participante})


# Em tests_views.py

def detalhe_grupo(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    participantes = Participante.objects.filter(grupo=grupo)
    
    # NOVO: Verifica se já existem sorteios para este grupo
    sorteios = Sorteio.objects.filter(grupo=grupo)
    ja_sorteado = sorteios.exists()
    
    return render(request, "grupos/detalhe_grupo.html", {
        "grupo": grupo, 
        "participantes": participantes,
        "ja_sorteado": ja_sorteado, # Mandamos essa informação para o HTML
        "sorteios": sorteios        # Mandamos a lista (opcional, para o admin ver)
    })

def sortear_amigo_secreto(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    participantes = list(Participante.objects.filter(grupo=grupo))

    if len(participantes) < 2:
        messages.error(request, "É necessário pelo menos 2 participantes.")
        return redirect("detalhe_grupo", grupo_id=grupo.id)

    random.shuffle(participantes)

    for i, p in enumerate(participantes):
        amigo_secreto_sorteado = participantes[(i + 1) % len(participantes)]
        
        # CORREÇÃO AQUI: Usar 'quem_tirou' e 'amigo' conforme o models.py
        Sorteio.objects.create(
            grupo=grupo,
            quem_tirou=p,              # Antes estava 'participante'
            amigo=amigo_secreto_sorteado # Antes estava 'amigo_secreto'
        )
        
    return redirect("detalhe_grupo", grupo_id=grupo.id)