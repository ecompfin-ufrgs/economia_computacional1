"""
Programa adulto
Descrição: Este programa pergunta a idade de uma pessoa. Se a
idade for maior do que 18 anos, o programa imprime na tela o texto
'Oi! Vocˆe ´e um adulto.'
Data: 26/03/2026
Versão: 0.1.0
"""

# Alocação de memória

idade = 0
texto = ""

# Entrada de dados

idade = int(input("\nQual a sua idade? "))

# Processamento de dados

if idade >= 18:
    texto = 'Oi! Você é um adulto.'


# Saída de dados

print(texto)
