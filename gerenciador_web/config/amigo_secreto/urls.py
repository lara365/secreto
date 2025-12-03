# amigo_secreto/urls.py (Sugestão baseada nas views)
from django.urls import path
from . import tests_views  # ou views

urlpatterns = [
    path('grupos/', tests_views.listar_grupos, name='listar_grupos'),
    path('grupos/criar/', tests_views.criar_grupo, name='criar_grupo'),
    path('grupos/<int:grupo_id>/', tests_views.detalhe_grupo, name='detalhe_grupo'),
    path('grupos/<int:grupo_id>/entrar/', tests_views.entrar_no_grupo, name='entrar_no_grupo'),
    path('participantes/<int:participante_id>/desejos/', tests_views.cadastrar_lista_desejos, name='cadastrar_lista_desejos'),
    path('grupos/<int:grupo_id>/sortear/', tests_views.sortear_amigo_secreto, name='sortear_amigo_secreto'),
]