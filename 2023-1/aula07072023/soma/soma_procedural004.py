# Definindo os objetos (atribuição de variáveis)




# Função para entrada de dados
def leitora_numeros():
    i = 0
    numeros = []
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


    
def main():
    # Atribuição de variáveis
    numeros = []
    soma = 0
    
    # Entrada de dados
    numeros = leitora_numeros()
    
    # Processamento de dados
    soma = adicao(numeros[0], numeros[1])
    
    # Saída de dados
    escritora_numeros(numeros[0], numeros[1], soma)
    
    
    
# Invocando a função principal

if __name__ == "__main__":
    main()


























