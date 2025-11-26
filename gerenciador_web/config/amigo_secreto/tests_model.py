from django.shortcuts import render, redirect, get_object_or_404
from .models import Grupo
from django.http import HttpResponse

def listar_grupos(request):
    
    
    grupos_salvos = Grupo.objects.all()
    
    
    contexto = {
        'meus_grupos': grupos_salvos
    }

    
    return render(request, 'grupos/lista.html', contexto)


