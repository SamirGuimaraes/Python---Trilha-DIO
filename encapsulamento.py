class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo
    
conta = Conta("0001", 100)
conta.depositar(100)
print(f"Número da agência: {conta.nro_agencia}")
print(f"Saldo atual: R${conta.mostrar_saldo()}")