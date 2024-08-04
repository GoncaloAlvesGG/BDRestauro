from django.shortcuts import render, redirect
from django.contrib import messages
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
    return render(request,
        "register.html",
    )

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM login_utilizador(%s,%s)", [email, password])
            result = cursor.fetchone()
        if result:
            id_utilizador = result[0]
            primeiro_nome = result[1]
            admin = result[2]
            status = result[3]

            if status == 'success':
            # Process successful login, e.g., create a session or return user data
                request.session["id_utilizador"] = id_utilizador
                request.session["nome"] = primeiro_nome
                request.session["admin"] = admin
                return redirect('principal')
            
            else:
            # Handle login failure
                messages.error(request, 'Email ou Password Inválida')
        else:
            messages.error(request, 'Email ou Password Inválida')
    return redirect('login')

def logout_user(request):
    try:
        del request.session["id_utilizador"]
        del request.session["nome"]
        del request.session["admin"]
        return redirect("/")
    except KeyError:
        pass
    return redirect("/")


def login(request):
    if request.method == 'POST':
        return login_user(request)
    else:
        return render(request, 'login.html')

def principal(request):
    return render(request,
        "principal.html",
    )

