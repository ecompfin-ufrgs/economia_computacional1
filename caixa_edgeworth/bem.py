from typing import List

class Bem:
    def __init__(self, nome: str, quantidade: float = 0, preco: float = 0) -> None:
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        

class Cesta:
    def __init__(self, lista_bens: List[Bem]) -> None:
        self.lista_bens = lista_bens
    def __repr__(self) -> str:
        return f"A cesta de consumo é uma lista de objetos da classe Bem"
    def calcula_valor_cesta(self) -> float:
        for bem in lista_bens:
            valor += lista_bens[bem.quantidade]*bem.preco
        return valor
    