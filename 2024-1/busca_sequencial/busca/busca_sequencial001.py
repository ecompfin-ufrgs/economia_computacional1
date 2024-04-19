"""
Programa busca_sequencial.py
Descrição: Este programa busca um valor em uma base de dados.
Autor: Nelson Seixas dos Santos
Versão: 0.0.1
Data: 19/04/2024
"""

## Alocação de memória

lista = []
achou = False
posicao = 0
cpf = 0


# Leitura da base de dados de cpf

base = [1,5,2,87,31]
lista = base

# Leitura de dados

cpf = int(input("Digite o valor a procurar: "))

# Processamento de dados

while posicao < len(lista):
    if lista[posicao] == cpf:
        achou = True
        break
    posicao += 1 # é a mesma coisa que posicao = posicao + 1

# Saída de dados

if achou:
    print(f'\nO valor {cpf} foi achado na posição {posicao}.')
else:
    print(f'\nO valor {cpf} não foi achado.')
