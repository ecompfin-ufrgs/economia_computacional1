


# Definição de variáveis
i = 0
numeros = [0,0]
soma = 0

# Entrada de dados
while i < 2:
    numeros[i] = int(input(f'\nDigite a parcela {i+1}: '))
    i+=1

# Processamento de dados
for numero in numeros:
    soma+=numero

# Saída de dados
print(f'\nA soma do número {numeros[0]} com o número {numeros[1]} é igual a {soma}.')