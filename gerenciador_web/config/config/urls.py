from django.urls import path
from . import views

urlpatterns =[
    urlpatterns = [
    path('', views.listar_grupos, name='listar_grupos'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('listas-desejos/', views.listar_listas_desejos, name='listar_listas_desejos'),
    path('sorteios/', views.listar_sorteios, name='listar_sorteios'),
]


]