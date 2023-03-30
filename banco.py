class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self.saldo += valor
        self.depositos.append(valor)

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        if valor > 500:
            raise ValueError("O valor máximo de saque diário é R$ 500,00")
        if len(self.saques) >= 3:
            raise ValueError("Número máximo de saques diários atingido")
        if self.saldo < valor:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        self.saques.append(valor)

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")

