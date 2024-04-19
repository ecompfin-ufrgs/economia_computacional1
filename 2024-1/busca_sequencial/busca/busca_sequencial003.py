"""
Programa busca_sequencial.py
Descrição: Este programa busca um valor em uma base de dados.
Autor: Nelson Seixas dos Santos
Versão: 0.0.3
Correção realizadas:
1. informação mais intuitiva ao usuária da posição em que seu cpf foi encontrado.
2. informação mais precisa de que o valor procurado é um cpf.
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

cpf = int(input("Digite o CPF a procurar: "))

# Processamento de dados

while posicao < len(lista):
    if lista[posicao] == cpf:
        achou = True
        break
    posicao += 1 # é a mesma coisa que posicao = posicao + 1

# Saída de dados

if achou:
    print(f'\nO CPF {cpf} foi achado na posição {posicao + 1}.')
else:
    print(f'\nO CPF {cpf} não foi achado.')
