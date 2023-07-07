# Definindo os objetos (atribuição de variáveis)

numeros = []

soma = 0

i = 0 # contador de números

# Função para entrada de dados

def leitora_numeros():
    i = 0
    while i < 2:
        numeros.append(float(input(f"Digite o número {i + 1}: ")))
        i+=1
    return numeros


# Função para processamento de dados
def adicao(x, y):
    return x + y


# função para saída de dados

def escritora_numeros(x, y, z):
    print(f"A soma do numero {x} com o número {y} é igual a {z}.")


    
# Invocando as funções definidas para executar o código

# Entrada de dados
numeros = leitora_numeros()

# Processamento de dados

soma = adicao(numeros[0], numeros[1])


# Saída de dados

escritora_numeros(numeros[0], numeros[1], soma)





















