# Alocação de memória

idade = 0
frase = ""

# Entrada de dados
idade = int(input("Qual a sua idade?"))

# Processamento de dados

if idade < 13:
    frase = "Oi!  Voce eh uma crianca."
elif idade >= 13 or idade <= 17:
    frase = "Oi, Voce eh um adolescente."
else:
    frase = "Voce eh adulto."

# Saída de dados

print(frase)
