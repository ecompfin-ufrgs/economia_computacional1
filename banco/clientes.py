class Cliente:
    """Classe que modela clientes do banco."""
    def __init__(self, nome: str, telefone: str) -> None:
        self.nome = nome
        self.telefone = telefone
    