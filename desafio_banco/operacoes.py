import datetime
from db_mock import clientes


class Operacoes:
    def __init__(self, id_cliente, senha_cliente, limite, limite_saques):
        self.id_cliente = id_cliente
        self.limite = limite
        self.limite_saques = limite_saques
        self.clientes = clientes
        self.cliente = None
        self.numero_saques = 0
        self.senha_cliente = senha_cliente

    def logar_cliente(self):
        for cliente in self.clientes:
            if (
                cliente.get("idCliente") == self.id_cliente
                and cliente.get("senhaCliente") == self.senha_cliente
            ):
                self.cliente = cliente
                print("Cliente logado com sucesso!")
                continue
        if not self.cliente:
            print("Usuário ou senha incorreta.")

    def depositar(self):
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            self.cliente["saldoCliente"] += valor
            self.cliente["lsExtratoCliente"].append(
                f"Depósito: R$ {valor:.2f}  - Data: {datetime.datetime.now()}"
            )
            print(f"Depósito: R$ {valor:.2f} realizado com sucesso")

        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self):
        valor = float(input("Informe o valor do saque: "))

        if valor > self.cliente["saldoCliente"]:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif self.numero_saques >= self.limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            self.cliente["saldoCliente"] -= valor
            self.cliente["lsExtratoCliente"].append(
                f"Saque: R$ {valor:.2f} - Data: {datetime.datetime.now()}"
            )
            self.numero_saques += 1
            print("Saque efetuado com sucesso.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    def solicitar_extrato(self):
        saldo_cliente = self.cliente["saldoCliente"]
        print("\n================ EXTRATO ================")
        if self.cliente["lsExtratoCliente"]:
            for operacao in self.cliente["lsExtratoCliente"]:
                print(operacao)
            print(f"\nSaldo: R$ {saldo_cliente:.2f} - Data: {datetime.datetime.now()} ")

        else:
            print("Não foram realizadas movimentações.")
        print("==========================================")
