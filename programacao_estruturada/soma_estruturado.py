
"""Programa soma_estruturado
Descrição
Este programa soma dois números, usando a estrutura de controle de fluxo de execução while.

Autor: Nelson S. dos Santos
Data: 02/04/2025
Versão: 0.0.1
"""

# Alocacao de memoria
parcela= 0
soma = 0

# Entrada e processamento de dados
while parcela < 2:
  num = int(input(f'Informe a parcela {parcela + 1}')) # entrada
  soma = soma + num # processamento com acumulador
  parcela = parcela + 1 # contador de parcelas

# Saida de dados
print('A soma dos numeros eh igual a:', soma)
