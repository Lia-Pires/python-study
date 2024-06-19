from operacoes import Operacoes


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

LIMITE = 500
LIMITE_SAQUES = 3


id_cliente = str(input("Informe sua id:"))
senha_cliente = str(input("Informe sua senha:"))
operacoes = Operacoes(id_cliente, senha_cliente, LIMITE, LIMITE_SAQUES)
operacoes.logar_cliente()

while True:
    opcao = input(menu)

    if opcao == "d":
        operacoes.depositar()

    elif opcao == "s":
        operacoes.sacar()

    elif opcao == "e":
        operacoes.solicitar_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
