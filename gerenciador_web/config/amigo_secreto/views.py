from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Grupo, Participante, ListaDesejos, Sorteio
import random


def listar_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'grupos/lista.html', {'grupos': grupos})


def criar_grupo(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_sorteio = request.POST.get('data_sorteio')
        valor_limite = request.POST.get('valor_limite')

        if not nome:
            messages.error(request, "O nome do grupo é obrigatório.")
            return redirect('criar_grupo')

        grupo = Grupo.objects.create(
            nome=nome,
            data_sorteio=data_sorteio,
            valor_limite=valor_limite
        )

        messages.success(request, "Grupo criado com sucesso!")
        return redirect('listar_grupos')

    return render(request, 'grupos/criar.html')


def listar_usuarios(request):
    usuarios = Participante.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})


def listar_listas_desejos(request):
    listas = ListaDesejos.objects.all()
    return render(request, 'listas/lista.html', {'listas': listas})


def listar_sorteios(request):
    sorteios = Sorteio.objects.all()
    return render(request, 'sorteios/lista.html', {'sorteios': sorteios})


def realizar_sorteio(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    participantes = list(Participante.objects.filter(grupo=grupo))

    if len(participantes) < 2:
        messages.error(request, "É necessário pelo menos 2 participantes para sortear.")
        return redirect('listar_grupos')

    sorteados = participantes.copy()
    random.shuffle(sorteados)

    tentativas = 0
    while any(participantes[i].id == sorteados[i].id for i in range(len(participantes))):
        random.shuffle(sorteados)
        tentativas += 1
        if tentativas > 50:
            messages.error(request, "Erro ao sortear. Tente novamente.")
            return redirect('listar_grupos')

    for i in range(len(participantes)):
        Sorteio.objects.create(
            grupo=grupo,
            quem_tirou=participantes[i],
            amigo=sorteados[i]
        )

    messages.success(request, "Sorteio realizado com sucesso!")
    return redirect('listar_sorteios')