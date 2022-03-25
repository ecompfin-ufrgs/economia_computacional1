# Herança em Python

class Animal:
    """Classe pai a partir da qual serão
criadas classe filho que herdarão desta classe.
"""
    def __init__(self, nome, numero_patas):
        self.numero_patas = numero_patas
        self.nome = nome
    def andar(self):
        pass
    def falar(self):
        pass


class Cachorro(Animal):
    def __init__(self, nome, numero_patas):
        Animal.__init__(self, nome, numero_patas)
    def andar(self):
        print("O cachorro está andando.")
    def falar(self):
        print("Au au!")

class Gato(Animal):
    def __init__(self, nome, numero_patas):
        Animal.__init__(self, nome, numero_patas)
    def andar(self):
        print("O gato está andando.")
    def falar(self):
        print("Miau")
    
    


class Cavalo(Animal):
    def __init__(self, nome, numero_patas, cor_do_focinho):
        super().__init__(nome, numero_patas)
    def pastar(self):
        print("A cavalo está pastando.")
    def andar(self):
        print(f"{self.nome} está trotando.")


boby = Cachorro("boby", 4)
napoleao = Gato("napoleao", 3)
pedro = Cavalo("pedro", 4, "preto")


boby.andar()
napoleao.andar()

boby.falar()
napoleao.falar()
pedro.pastar()
pedro.andar()


