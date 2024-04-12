"""
Programa conv_dist

Descrição: Este programa lê um valor em metros e o converte para milíımetros.
Autor: Nelson S. dos Santos
Data: 12/04/2024
Versão: 1.0.0

"""


# Alocação de memória

metros: float = 0

milimetros: float = 0

# Entrada de dados

metros = float(input("Digite a distância em metros. "))

# Processamento de dados

milimetros = 1000*metros


# Saída de dados

print(f'\nA distância em milímetros é igual a {milimetros}.')