#Alocacao de memoria
soma: float = 0.0
valor: float = 0.0
i: int = 0
num_val: int = 0

#### Entrada e processamento de dados
num_val = int(input("Qual o numero de valores?\n"))

while i < num_val:
    valor = float(input(f"Digite numero {i+1}.\n"))
    soma = soma + valor
    i = i + 1
    media = soma/num_val

# Saida de dados    
print('A media dos numeros eh igual a %5.2f:'%media)  
