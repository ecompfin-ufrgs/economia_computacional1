

# Leitura de dados

grau = int(input("\nDigite o grau do polinômio: "))
ponto = float(input("\nDigite o ponto onde você deseja calcular o valor do polinômio: "))

# leitura dos coeficientes do polinômio
lista_coeficientes = []
i = 0
while i < grau + 1:
    lista_coeficientes.append(float(input(f"\nDigite o coeficiente de grau {i}: ")))
    i+=1

# Cálculo do valor do polinômio

i = 0
polinomio = 0
while i < len(lista_coeficientes):
    polinomio = polinomio + lista_coeficientes[i]*(ponto)**(i)
    i+=1

# Saída de dados

print(f'\nO valor do polinômio no ponto {ponto} é igual a {polinomio}.')

            
