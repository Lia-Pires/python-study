from usuario import *
import os

def selecionar_conta(usuario):
    print("\n===== Suas Contas =====")
    for i, conta in enumerate(usuario.contas, start=1):
        print(f"{i}. Agência: {conta.agencia} | Conta: {conta.id_conta}")
    print("========================")

    escolha = input(": ")
    if not escolha.isdigit():
        print("Escolha inválida.")
        return None

    conta_index = int(escolha) - 1
    if 0 <= conta_index < len(usuario.contas):
        return usuario.contas[conta_index]
    else:
        print("Escolha inválida.")
        return None

def usuario_deposito(usuario):
    valor = float(input("Digite o valor que deseja depositar: "))
    transacao = Deposito(valor)
    conta = selecionar_conta(usuario)
    
    if not conta:
        return
    
    usuario.realizar_transacao(conta, transacao)

def withdraw_usuario(usuario):
    valor = float(input("Informe o valor que deseja sacar: "))
    transacao = Saque(valor)
    conta = selecionar_conta(usuario)
    
    if not conta:
        return
    
    usuario.realizar_transacao(conta, transacao)

def conta_usuario(usuario):
    conta = selecionar_conta(usuario)
    
    if not conta:
        return
    
    print("\n================ EXTRATO ================")
    transacaos = conta.historico.transacaos

    statement = ""
    if not transacaos:
        statement = "Nenhuma transação foi realizada."
    else:
        for transacao in transacaos:
            statement += f"\n{transacao['type']}:\n\t$ {transacao['valor']:.2f} - {transacao['date']}"

    print(statement)
    print(f"\nSaldo:\n\t$ {conta.balance:.2f}")
    print("==========================================")

def new_conta_usuario(usuario, contas):
    conta_id = len(contas) + 1
    conta_type = input("Escolha o tipo de conta (1 para conta corrente): ")
    conta_usuario = conta.new_conta(usuario, conta_id, type_conta=conta_type)

    if not conta_usuario:
        return

    usuario.add_conta(conta_usuario)
    contas.append(conta_usuario)
    print("\n=== Nova conta criada com sucesso! ===")

def list_contas_usuario(usuario):
    print("\n===== Lista de Contas =====")
    for conta in usuario.contas:
        print(f"Agencia: {conta.agencia} | Conta: {conta.id_conta}")
    print("========================")

def navegation_conta(usuario):
    while True:
        conta_menu()
        option = input("=> ")
        clear_screen()

        if option == "d":
            usuario_deposito(usuario)

        elif option == "s":
            withdraw_usuario(usuario)

        elif option == "e":
            conta_usuario(usuario)
        
        elif option == "nc":
            new_conta_usuario(usuario)

        elif option == "lc":
            list_contas_usuario(usuario)

        elif option == "q":
            print(f"Até logo {usuario.name}! \n Volte sempre")
            break

        else:
            print("Opção inválida. Tente novamente. \n")

def initial_menu():
    print("""

    ================ Banco GC ================

        Escolha uma opção:

        [1] - Fazer Login
        
        [2] - Criar novo Usuário

        [3] - Sair do App
        
        """)
    
def conta_menu():
    print("""
            ================ MENU ================
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [nc] Nova Conta
            [lc] Listar Contas
            [q] Sair

        """)
            
def clear_screen():
    os.system("cls") or None

def create_usuario():
    endereco = input("Digite um endereço: ")
    email = input("Digite um email: ")
    senha = input("Escolha uma senha: ")
    nome = input("Informe seu nome: ")
    nascimento = input("Informe sua data de Nascimento: ")
    cpf = input("Informe seu CPF: ")
    usuarios = []

    new_usuario = Usuario.create_usuario(endereco, email, senha, name=nome, birthday=nascimento, cpf=cpf)
    usuarios.append(new_usuario)

def login():
        
    email = input("Digite seu email: ")
    password = input("Digite sua Senha: ")
    authenticated_usuario = Usuario.authenticate(email, password)

    while not authenticated_usuario:
        print("Usuário ou senha inválidos\n")
        email = input("Digite seu email: ")
        password = input("Digite sua Senha: ")
        authenticated_usuario = Usuario.authenticate(email, password)

    navegation_conta(authenticated_usuario)


while True:

    initial_menu()

    opcao = input("=> ")
    clear_screen()

    if opcao == "1":
        login()

    elif opcao == "2":
        create_usuario()

    elif opcao == "3":
        print("Volte sempre!!\n")
        break

    else:
        print("Digite uma opção válida: ")