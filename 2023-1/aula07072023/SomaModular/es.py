"""
Programa es
Descrição: Este módulo prover funcionalidades de entrada e saída de dados para o programa soma_modular.py
Autor: Eu
Data: 07/07/2023
Versão: 0.0.1
"""

# Função para entrada de dados
def leitora_numeros():
    i = 0
    numeros = []
    while i < 2:
        numeros.append(float(input(f"Digite o número {i + 1}: ")))
        i+=1
    return numeros



# função para saída de dados
def escritora_numeros(x, y, z):
    print(f"A soma do numero {x} com o número {y} é igual a {z}.")
