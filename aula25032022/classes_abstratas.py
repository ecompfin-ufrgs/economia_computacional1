# Herança com classes abstratas


"""
Classe abstrata 


"""

# Exemplo 1: criação de classe abstrata por método ingênuo

class Empregado:
    def __init__(self, nome):
        self.nome = nome
    def trabalhar(self):
        pass

joao = Empregado("João")
joao.trabalhar()


# Exemplo 2: criação de classe abstrata por meio da pacote abc da biblioteca padrão


from abc import ABC, abstractmethod


class Empregado_Abstrato(ABC):
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    @abstractmethod
    def trabalhar(self):
        pass

# empregado = Empregado_Abstrato("Empregado", "Emprego")
# empregado.trabalhar()

class Gerente(Empregado_Abstrato):
    def __init__(self, nome, cargo):
        super().__init__(nome, cargo)
    def trabalhar(self):
        print("Estou coordenando os analistas.")
    def mandar(self):
        print("Estou mandando os analistas trabalharem.")
        
guilherme = Gerente("Guilherme", "Gerente Nível I")
guilherme.trabalhar()
guilherme.mandar()

class Analista(Empregado_Abstrato):
    def __init__(self, nome, cargo):
        super().__init__(nome, cargo)
    def trabalhar(self):
        print("Estou analisando.")

lucas = Analista("Lucas", "Analista Júnior")
lucas.trabalhar()

