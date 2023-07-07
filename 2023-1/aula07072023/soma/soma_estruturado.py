# Atribuição de variáveis

numeros = []

soma = 0

i = 0 # contador de números



# Entrada de dados

while i < 2:
    numeros.append(float(input(f"Digite o número {i + 1}: ")))
    i+=1

    
# Processamento de dados 

for numero in numeros:
    soma+=numero
    
# Saída de dados

print(f"A soma do numero {numeros[0]} com o número {numeros[1]} é igual a {soma}.")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    