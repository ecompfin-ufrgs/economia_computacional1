"""
Programa soma
Descrição: Este programa lê dois números inteiros digitados pelo usuário e p~e na tela a soma deles.
Autor: Eu
Data: 12/04/2024
Versão: 0.0.2
"""

# Alocação de memória

i: int = 0

numero: int = 0

soma: int = 0




# Entrada e processamento de dados


while i < 2:
    numero = int(input(f"Digite a parcela {i+1}: "))
    soma = soma + numero
    i+=1


# Saída de dados


print(f'A soma dos números digitados é igual a {soma}.')