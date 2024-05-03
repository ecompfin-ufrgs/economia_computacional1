
# Definição de funções


# Função para entrada de dados
def entrada_dados():
    dados = []
    i = 0
    while i < 2:
        dados.append(int(input(f'\nDigite a parcela {i + 1}: ')))
        i+=1
    return dados


# função para somar números
def soma(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado


# Definição da função de saida
def saida_dados(x):
    print(f'\nA soma é igual a {x}.')

# função principal
def main():
    dados = entrada_dados()
    resultado = soma(dados[0], dados[1])
    saida_dados(resultado)


# Execução da função principal
main()