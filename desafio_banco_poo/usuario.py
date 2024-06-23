from abc import ABC, abstractmethod
import datetime


class Usuario:
    def __init__(self, endereco, email, senha):
        self.contas = []
        self.endereco = endereco
        self.email = email
        self.senha = senha

    def transacao(self, conta, transacao):
        transacao.register(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    @classmethod
    def create_usuario(cls, endereco, email, senha, **kwargs):
        if "name" in kwargs and "data_nascimento" in kwargs and "cpf" in kwargs:
            return Individual(endereco, email, senha, **kwargs)
        elif "name" in kwargs and "cnpj" in kwargs:
            return Legal_Entity(endereco, email, senha, **kwargs)
        else:
            raise ValueError("informações inválidas")

    @staticmethod
    def authenticate(email, senha, usuarios):
        for usuario in usuarios:
            if usuario.email == email and usuario.senha == senha:
                return usuario
        return None


class Individual(Usuario):
    def __init__(self, endereco, email, senha, name, data_nascimento, cpf):
        super().__init__(endereco, email, senha)

        self.name = name
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __str__(self):
        return f"Pessoa Física: {self.endereco}, {self.email}, {self.senha}, {self.name}, {self.data_nascimento}, {self.cpf}"


class Legal_Entity(Usuario):
    def __init__(self, endereco, email, senha, name, cnpj):
        super().__init__(endereco, email, senha)

        self.name = name
        self.cnpj = cnpj

    def __str__(self):
        return f"Pessoa Jurídica: {self.endereco}, {self.email}, {self.senha}, {self.name}, {self.cnpj}"

class conta:
    def __init__(self, id_conta, usuario):
        self._balance = 0
        self._agencia = "0001"
        self._historico = historicoo()
        self._id_conta = id_conta
        self._usuario = usuario

    @classmethod
    def nova_conta(cls, usuario, id_conta, type_conta):
        if type_conta == "1":
            return conta_atual(id_conta, usuario, type_conta)
        else:
            print("Tipo inválido, selecione um tipo válido")
            return None

    @property
    def saldo(self):
        return self._balance

    @property
    def id_conta(self):
        return self._id_conta

    @property
    def agencia(self):
        return self._agencia

    @property
    def usuario(self):
        return self._usuario

    @property
    def historicoo(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        valor_excedido = valor > saldo

        if valor_excedido:
            print("\n Falha na operação, você não tem saldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print("\n Saque realizado com sucesso!")
            return True

        else:
            print("Falha! Valor inválido.")
            return False

    def deposito(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")

        else:
            print("Falha na operação! Valor inválido")
            return False

        return True


class conta_atual(conta):
    def __init__(
        self, id_conta, usuario, tipo_conta, limite_valor=500, limite_saque=3
    ):
        super().__init__(id_conta, usuario)
        self._limite_valor = limite_valor
        self._limite_saque = limite_saque
        self._tipo = tipo_conta

    def saque(self, valor):
        valor_saque = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["type"] == Saque.__name__
            ]
        )

        limite_excedido = valor > self._limite_valor
        limite_saque_excedido = valor_saque >= self._limite_saque

        if limite_excedido:
            print(
                "Falha! o valor do Saque excede o limite permitido para sua conta."
            )

        elif limite_saque_excedido:
            print("Falha! Número máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
                Agência:\t{self.agencia}
                C/C:\t\t{self.id_conta}
                Titular:\t{self.usuario.name}
                """


class historicoo:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def add_transacao(self, transacao):
        self._transacoes.append(
            {
                "type": transacao.__class__.__name__,
                "valor": transacao.valor,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_success = conta.saque(self.valor)

        if transacao_success:
            conta.historicoo.add_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.deposit(self.valor)

        if sucesso_transacao:
            conta.historicoo.add_transacao(self)
