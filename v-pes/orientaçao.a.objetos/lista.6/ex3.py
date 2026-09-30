class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        return self.saldo


# Testando a classe
conta = ContaBancaria("Ignacio Kirhiako Sepulveda Ramirez")

conta.depositar(1000)
conta.depositar(500)
conta.sacar(300)

print("Titular:", conta.titular)
print("Saldo atual:", conta.mostrar_saldo())
