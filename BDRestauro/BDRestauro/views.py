from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')

def index(request):
    return render(request, 'index.html')

def tabela_users(request):
    if request.session.get('id_utilizador') is not None and request.session.get('admin') is True:
        utilizadores = listar_utilizadores(request.session.get('id_utilizador')),
        return render(
            request,
            "lista_utilizadores.html",
            {"utilizadores": utilizadores[0]},
    )
    else:
        messages.error(request, 'Não tem permissões para aceder a essa página!')
        return redirect(request.META.get('HTTP_REFERER', '/'))


def register(request):
    if request.method == 'POST':
        return register_user(request)
    else:
        return render(request, 'register.html')

def register_user(request):
    if request.method == 'POST':
        primeiro_nome = request.POST['primeiro_nome']
        ultimo_nome = request.POST['ultimo_nome']
        email = request.POST['email']
        password = request.POST['password']
        morada = request.POST['morada']
        telemovel = request.POST['telemovel']
        nif = request.POST.get('nif', None)  # Optional field
        admin = False

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    CALL add_utilizador_proc(%s, %s, %s, %s, %s, %s, %s, %s)
                """, [
                    primeiro_nome,
                    ultimo_nome,
                    email,
                    password,
                    morada,
                    telemovel,
                    admin,
                    nif
                ])
                messages.success(request, 'Registado com sucesso! Por favor autentique-se!')
                return redirect('login')
        except Exception as e:
            if 'O email já existe' in str(e):
                messages.error(request, 'O email já se encontra em uso!')
            else:
                messages.error(request, f'Erro a adicionar o utilizador: {str(e)}')

    return redirect('register')


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
        request.session.flush()
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

def registar_entrada(request):
    return render(request, 'registar_entrada.html')

def consultar(request):
    return render(request, 'consultar.html')

def registar_saida(request):
    return render(request, 'registar_saida.html')

def veiculos(request):
    return render(request, 'veiculos.html')

def historico(request):
    return render(request, 'historico.html')

def conta(request):
    return render(request, 'conta.html')