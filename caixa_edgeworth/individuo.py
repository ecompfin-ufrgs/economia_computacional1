from typing import List

class Individuo:
    def __init__(self, dotacao: List[Bem] = None) -> None:
        self.dotacao = dotacao
        if self.dotacao == None:
            self.riqueza = 0
        else:
            for bem in dotacao:
                riqueza += dotacao[bem.quantidade]*dotacao.preco
    def utilidade(self, dotacao) -> float:
        return (dotacao[0]**(0.5))(dotacao[1]**(0.5))