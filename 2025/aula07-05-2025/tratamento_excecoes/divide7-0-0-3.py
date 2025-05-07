"""Programa divide7
Descrição: 
Este programa lê um número dado pelo usuário e o utiliza como denominador da fração 7/d,
onde d é o número entrado pelo usuário.
Autor: Nelson S. dos Santos
Data: 07/05/2025
Versão: 0.0.3
Notas de atualização: Esta versão protege o código contra a exceção de divisão por zero, usando a cláusula try/except.
"""

# Importação de módulos

# import sys

# Alocação de memória

d = 0

# Entrada de dados

d = float(input("Digite um número: "))

    

#if d == 0:
#    print("\nNão é possível executar esta operação.  Não existe divisão por zero.")
#    sys.exit()

# Processamento de dados --- Cálculo de x
try:
    x = 7/d
except:
    print(f"\nNão foi possível calcular o resultado desejado.")
    exit()

# Saída de dados

print(x)


