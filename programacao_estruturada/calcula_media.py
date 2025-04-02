#Alocacao de memoria
soma: float = 0
valor: float = 0
i: int = 0
num_val: int = 0

# Entrada e processamento de dados
num_val = int(input("Qual o numero de valores?\n"))

while i < num_val:
    valor = float(input("Digite um numero.\n"))
    soma = soma + valor
    i = i + 1
    media = soma/numero_valores

# Saida de dados    
print('A media dos numeros eh igual a:', media)  
