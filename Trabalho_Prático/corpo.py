import csv
from collections import namedtuple
from getpass import getpass
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# ================= CONSTANTES =================
ARQUIVO_USUARIOS = "usuarios.txt"
USUARIO_LOGADO = None
console = Console()

# ================= FUNÇÕES DE USUÁRIO =================

def ler_usuarios(arquivo_csv):
    """
    Lê o arquivo de usuários e retorna um dicionário.
    chave: login
    valor: Usuario (namedtuple)
    """
    Usuario = namedtuple("Usuario", ["login", "senha", "tipo"])
    usuarios = {}

    with open(arquivo_csv, mode="r", newline="") as file:
        reader = csv.reader(file)
        for login, senha, tipo in reader:
            usuarios[login] = Usuario(login, senha, tipo)

    return usuarios


def fazer_login(usuarios):
    """
    Realiza o login do usuário.
    Atualiza a variável global USUARIO_LOGADO.
    """
    global USUARIO_LOGADO

    console.print(
        Panel(
            "🟢 LOGIN 🟢\n\nInforme suas credenciais.",
            title="Tela de Login",
            expand=False,
        )
    )

    login = Prompt.ask("Usuário")
    senha = getpass("Senha: ")

    usuario = usuarios.get(login)

    if usuario and usuario.senha == senha:
        USUARIO_LOGADO = usuario
        console.print("[bold green]Login realizado com sucesso![/bold green]")
    else:
        console.print("[bold red]Usuário ou senha inválidos![/bold red]")


def cadastrar_usuario(usuarios, arquivo_csv):
    """
    Cadastra um novo usuário no sistema.
    """
    console.print(
        Panel(
            "Cadastro de Novo Usuário",
            title="Cadastro",
            expand=False,
        )
    )

    login = Prompt.ask("Nome de usuário")
    senha = getpass("Senha: ")

    if USUARIO_LOGADO and USUARIO_LOGADO.tipo == "admin":
        tipo = Prompt.ask("Tipo", choices=["admin", "cliente"])
    else:
        tipo = "cliente"

    if login in usuarios:
        console.print("[bold red]Usuário já existe![/bold red]")
        return False

    with open(arquivo_csv, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([login, senha, tipo])

    console.print("[bold green]Usuário cadastrado com sucesso![/bold green]")
    return login


def excluir_usuario(usuarios, arquivo_csv):
    """
    Remove um usuário do arquivo.
    """
    console.print(
        Panel(
            "Exclusão de Usuário",
            title="Excluir",
            expand=False,
        )
    )

    login = Prompt.ask("Usuário a excluir")

    if login not in usuarios:
        console.print("[bold yellow]Usuário não encontrado![/bold yellow]")
        return False

    if login == USUARIO_LOGADO.login:
        console.print("[bold red]Você não pode excluir seu próprio usuário![/bold red]")
        return False

    with open(arquivo_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        for usuario in usuarios.values():
            if usuario.login != login:
                writer.writerow([usuario.login, usuario.senha, usuario.tipo])

    console.print("[bold green]Usuário excluído com sucesso![/bold green]")
    return True


def atualizar_senha(usuarios, arquivo_csv):
    """
    Atualiza a senha de um usuário.
    Admin pode alterar qualquer senha.
    Cliente altera apenas a própria.
    """
    if USUARIO_LOGADO.tipo == "admin":
        login = Prompt.ask("Usuário")
    else:
        login = USUARIO_LOGADO.login

    if login not in usuarios:
        console.print("[bold yellow]Usuário não encontrado![/bold yellow]")
        return False

    nova_senha = getpass("Nova senha: ")

    with open(arquivo_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        for usuario in usuarios.values():
            if usuario.login == login:
                writer.writerow([usuario.login, nova_senha, usuario.tipo])
            else:
                writer.writerow([usuario.login, usuario.senha, usuario.tipo])

    console.print("[bold green]Senha atualizada com sucesso![/bold green]")
    return True


# ================= MENUS =================

def menu_inicial():
    console.print(
        Panel(
            "1 - Login\n2 - Cadastro\n3 - Sair",
            title="Menu Inicial",
            expand=False,
        )
    )
    return Prompt.ask("Opção", choices=["1", "2", "3"])


def menu_interno():
    console.print(
        Panel(
            f"Bem-vindo, {USUARIO_LOGADO.login}",
            title="Menu Interno",
            expand=False,
        )
    )

    if USUARIO_LOGADO.tipo == "admin":
        console.print("1 - Atualizar senha")
        console.print("2 - Excluir usuário")
        console.print("0 - Logout")
        return Prompt.ask("Opção", choices=["0", "1", "2"])
    else:
        console.print("1 - Atualizar senha")
        console.print("0 - Logout")
        return Prompt.ask("Opção", choices=["0", "1"])


# ================= FLUXO PRINCIPAL =================

usuarios = ler_usuarios(ARQUIVO_USUARIOS)

while True:
    opcao = menu_inicial()

    if opcao == "1":
        fazer_login(usuarios)
    elif opcao == "2":
        novo = cadastrar_usuario(usuarios, ARQUIVO_USUARIOS)
        if novo:
            usuarios = ler_usuarios(ARQUIVO_USUARIOS)
            USUARIO_LOGADO = usuarios.get(novo)
    else:
        break

    while USUARIO_LOGADO:
        usuarios = ler_usuarios(ARQUIVO_USUARIOS)
        escolha = menu_interno()

        if escolha == "0":
            USUARIO_LOGADO = None
        elif escolha == "1":
            atualizar_senha(usuarios, ARQUIVO_USUARIOS)
        elif escolha == "2":
            excluir_usuario(usuarios, ARQUIVO_USUARIOS)

