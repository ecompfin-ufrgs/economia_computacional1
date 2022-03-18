class Conta:
    def __init__(self, clientes: Cliente, numero: str, saldo = 0) -> None:
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
    def