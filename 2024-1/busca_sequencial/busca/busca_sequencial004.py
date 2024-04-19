"""
Programa busca_sequencial.py
Descrição: Este programa busca um valor em uma base de dados.
Autor: Nelson Seixas dos Santos
Versão: 0.0.4
Correção realizadas:
1. informação mais intuitiva ao usuária da posição em que seu cpf foi encontrado.
2. informação mais precisa de que o valor procurado é um cpf.
3. Substitui-se o laço while pelo for para ganhar eficiência na busca e tornar o programa mais legível que a versão anterior em contrapartida perdeu-se a funcionalidade de informar a posição onde foi achado o cpf no banco de dados.
Data: 19/04/2024
"""


## Alocação de memória

lista = []
achou = False
cpf = 0


# Leitura da base de dados de cpf

base = [1,5,2,87,31]
lista = base

# Leitura de dados

cpf = int(input("Digite o CPF a procurar: "))

# Processamento de dados

for elem in lista:
    if elem == cpf:
        achou = True
        break
      

# Saída de dados

if achou:
    print(f'\nO CPF {cpf} foi achado.')
else:
    print(f'\nO CPF {cpf} não foi achado.')
