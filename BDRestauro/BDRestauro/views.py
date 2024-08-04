from django.shortcuts import render
from .utils import *

def index(request):
    return render(request, 'index.html')

def tabela_users(request):
    utilizadores = listar_utilizadores(1),
    return render(
        request,
        "lista_utilizadores.html",
        {"utilizadores": utilizadores[0]},
    )

def register(request):
    return

def login(request):
    return

