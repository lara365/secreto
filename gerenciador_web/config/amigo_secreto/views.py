from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto
from django.http import HttpResponse

def listar_projetos(request):
   
    projetos_salvos = Projeto.objects.all()
    
    
    contexto = {
        'meus_projetos': projetos_salvos 
    }

    return render(request, 'projetos/lista.html', contexto)

