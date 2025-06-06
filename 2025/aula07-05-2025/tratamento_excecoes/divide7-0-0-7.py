"""Programa divide7
Descrição: 
Este programa lê um número dado pelo usuário e o utiliza como denominador da fração 7/d,
onde d é o número entrado pelo usuário.
Autor: Nelson S. dos Santos
Data: 07/05/2025
Versão: 0.0.7
Notas de atualização: Esta versão protege o código contra a exceção de divisão por zero de modo procedural.
"""

# Importação de módulos

import sys

# Tratamento prévio

def trata_prev(d):
    if d == 0:
        print("\nNão é possível executar esta operação.  Não existe divisão por zero.")
        sys.exit()



# Entrada de dados

def entrada():
    d = float(input("Digite um número: "))
    return d

# Processamento de dados --- Cálculo de x

def divide7(d):
    trata_prev(d)
    return 7/d

# Saída de dados

def saida(x):
    print(x)

def main():
    denominador = entrada()
    resultado = divide7(denominador)
    saida(resultado)


# Execuçaõ

if __name__ == "__main__":
    main()

